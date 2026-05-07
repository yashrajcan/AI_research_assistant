# AI_research_assistant
This project is an AI-powered Research Assistant built using LangChain, FAISS, and HuggingFace Transformers . It allows users to upload a PDF and ask questions based on its content using a Retrieval-Augmented Generation (RAG) pipeline.


## 🧠 How it works
1. Upload a PDF file  
2. Text is extracted using PyPDFLoader  
3. Text is split into chunks  
4. Embeddings are created using HuggingFace model  
5. FAISS stores vector embeddings  
6. Retriever finds relevant chunks  
7. FLAN-T5 generates answers based on context  

---

## 🛠️ Tech Stack
- Python
- Streamlit
- LangChain
- FAISS
- HuggingFace Transformers
- Sentence Transformers
