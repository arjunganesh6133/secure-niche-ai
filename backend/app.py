from fastapi import FastAPI, UploadFile, Form, File
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.llms import Ollama
import os

app = FastAPI(title="Secure Niche Specialist")

# --- Initialize embedding and DB ---
# We use a standard path so data persists across restarts
embedding_model = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
CHROMA_PATH = "backend/embeddings"
os.makedirs(CHROMA_PATH, exist_ok=True)

db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_model)

@app.post("/upload")
async def upload_doc(file: UploadFile = File(...)):
    # Ensure the directory exists
    os.makedirs("backend/documents", exist_ok=True)
    
    # Save the file locally
    file_path = f"backend/documents/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Load and process the PDF
    loader = PyPDFLoader(file_path)
    docs = loader.load()

    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=200)
    chunks = splitter.split_documents(docs)

    # Add to database
    db.add_documents(chunks)
    # Note: New versions of Chroma auto-persist, but we keep this just in case
    db.persist()
    
    return {"message": "File indexed successfully"}

@app.post("/query")
async def query_docs(question: str = Form(...)):
    # 1. Search for relevant text in the PDF
    retriever = db.as_retriever(search_kwargs={"k": 3})
    
    # FIX #1: Use invoke() instead of get_relevant_documents
    results = retriever.invoke(question)
    
    # Combine the found text into a single context string
    context = "\n".join([r.page_content for r in results])

    # FIX #2: Use 'tinyllama' to fit in your 3.1GB RAM (prevents 500 crash)
    llm = Ollama(model="tinyllama")
    
    # Ask the AI
    query_text = f"Answer using context:\n{context}\nQuestion: {question}"
    response = llm.invoke(query_text)
    
    return {"response": response}