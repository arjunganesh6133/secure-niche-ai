import streamlit as st
import requests

# Define the backend URL
BACKEND_URL = "http://127.0.0.1:8000"

st.title("🔒 Secure Niche Specialist AI")

# --- Step 1: File Upload Section ---
uploaded_file = st.file_uploader("Upload a document (PDF)", type=["pdf"])

if uploaded_file:
    files = {"file": uploaded_file.getvalue()}
    try:
        response = requests.post(f"{BACKEND_URL}/upload", files={"file": uploaded_file})
        if response.status_code == 200:
            st.success(response.json().get("message", "File uploaded successfully!"))
        else:
            st.error("Failed to upload file to backend.")
    except Exception as e:
        st.error(f"Connection Error during upload: {e}")

# --- Step 2: Q&A Section ---
query = st.text_input("Ask a question:")

if st.button("Ask"):
    if query:
        try:
            # FIX APPLIED HERE: We switched back to 'data=' because your backend expects Form Data
            response = requests.post(f"{BACKEND_URL}/query", data={"question": query})
            
            if response.status_code == 200:
                # Display the answer safely
                answer = response.json().get("response", "No answer found.")
                st.write(answer)
            else:
                # Show detailed error if something goes wrong
                st.error(f"Backend Error ({response.status_code}): {response.text}")
                
        except Exception as e:
            st.error(f"Connection Error: {e}")
    else:
        st.warning("Please enter a question first.")