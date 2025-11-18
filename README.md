# 🔒 Secure Niche Specialist AI
THE PROBLEM*
Hight-task professionals(lawyers,doctors,grant writers,financial analysts) cannot use ChatGPT because of privacy(HIPAA,attorney-client privilege).Generic RAG is also not good enough because the style and terminology must be perfect.

THE APP IDEA:
A "Private-cloud AI"that you install for them,fine-tuned on their data and RAG-powered by their document.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-green)
![LangChain](https://img.shields.io/badge/Orchestration-LangChain-yellow)
![Ollama](https://img.shields.io/badge/AI-Ollama%20(Local)-black)

A fully local, privacy-focused **RAG (Retrieval-Augmented Generation)** application designed for professionals who handle sensitive data. 

Unlike cloud-based tools (like generic ChatGPT), this application runs entirely on your machine, ensuring that **no data ever leaves your computer**.

## 🌟 Key Features

- **100% Offline Privacy:** Your documents are processed locally using Ollama.
- **PDF RAG Engine:** Upload PDF documents and chat with them instantly.
- **Vector Embeddings:** Uses `all-MiniLM-L6-v2` and **ChromaDB** for precise information retrieval.
- **Split Architecture:** Built with a decoupled **Streamlit** frontend and **FastAPI** backend for scalability.

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Backend:** FastAPI & Uvicorn
- **LLM Engine:** Ollama (Running `tinyllama` for efficiency)
- **Vector Database:** ChromaDB
- **Orchestration:** LangChain Community

## 📋 Prerequisites

Before running the app, ensure you have the following installed:
1. **Python 3.8+**
2. **[Ollama](https://ollama.com/)** (Must be running in the background)

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone [https://github.com/arjunganesh6133/secure-niche-ai.git](https://github.com/arjunganesh6133/secure-niche-ai.git)
   cd secure-niche-ai

   📝 Usage Guide
Upload: Drag and drop a PDF file (e.g., a resume, legal doc, or medical report).

Index: Wait for the green "File indexed successfully" message.

Ask: Type a specific question about the document (e.g., "What is the candidate's GPA?" or "Summarize the introduction").

Result: The local AI retrieves the exact context and generates an answer
