# 📚 AI Research Assistant (RAG Project)

## 🚀 Overview
This project is an AI-powered Research Assistant built using **LangChain, FAISS, and HuggingFace Transformers**.  
It allows users to upload a PDF and ask questions based on its content using a Retrieval-Augmented Generation (RAG) pipeline.

---

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

---
.

🧠 What is LangChain (in simple words)

👉 LangChain is a toolkit that helps you connect an LLM (like FLAN-T5 or GPT) with your own data and tools.

On its own, an LLM:

knows general knowledge
cannot read your PDF
cannot search your documents

LangChain fixes that by letting you build a pipeline:

Your data → processed → retrieved → sent to LLM → answer generated

🔥 In YOUR project (very important)

You built a RAG system using LangChain.

Let’s map your code step-by-step.

📌 1. Document Loader (LangChain start)
File:
loader.py
What you use:
PyPDFLoader
What LangChain is doing here:

👉 It reads your PDF and converts it into “documents”

So now:

PDF → text chunks
📌 2. Embeddings (LangChain + HuggingFace)
File:
embeddings.py
Code:
HuggingFaceEmbeddings
What it does:

👉 Converts text into numbers (vectors)

Why?
Because AI cannot compare text directly — it compares meaning using vectors.

So now:

Text → Vector representation
📌 3. Vector Store (FAISS via LangChain)
File:
vector_store.py
Code:
FAISS.from_documents()
What it does:

👉 Stores all document vectors in a searchable database

So now:

Vectors → stored in FAISS index
📌 4. Retriever (VERY IMPORTANT LangChain concept)
File:
retriever.py
What it does:

👉 Takes user question → finds most relevant chunks from FAISS

So now:

Question → relevant PDF text

This is the “retrieval” part of RAG

📌 5. Chain (LangChain core concept)
File:
chains.py

This is where LangChain concept is most visible.

You built:

qa_chain(query)
What happens here:
Get question
Retrieve relevant docs
Build prompt
Send to LLM (FLAN-T5)
Return answer

So now:

Question + Context → LLM → Answer
📌 6. Streamlit App (UI layer)
File:
app.py

This is NOT LangChain.

This is just:
👉 interface to interact with your LangChain pipeline

🔥 FULL FLOW OF YOUR PROJECT

This is your complete RAG system:

User Question
      ↓
Streamlit UI
      ↓
Retriever (LangChain)
      ↓
FAISS Vector DB (LangChain)
      ↓
Embeddings (LangChain)
      ↓
PDF Loader (LangChain)
      ↓
Relevant Text Context
      ↓
LLM (FLAN-T5 via Transformers)
      ↓
Final Answer
🧠 Simple explanation of LangChain in YOUR project

👉 LangChain is acting like the “manager” of the whole AI pipeline

It handles:

✔ reading PDF
✔ splitting data
✔ converting to embeddings
✔ storing in vector DB
✔ retrieving relevant info
✔ connecting to LLM

🧠 How I am using LangChain in this project

In this project, LangChain is used as the core framework to build a Retrieval-Augmented Generation (RAG) system that allows users to ask questions from a PDF.

It helps connect document loading, embedding creation, vector storage, retrieval, and question answering into a single pipeline.

🔥 Step-by-step usage of LangChain in my project
1. 📄 Document Loading (LangChain Loader)

I use LangChain’s document loader:

PyPDFLoader
What it does:
Reads the uploaded PDF
Converts each page into a Document object
Extracts text from the file

👉 So LangChain is responsible for turning PDF into usable text data

2. ✂️ Text Processing (Document Objects)

LangChain stores PDF content as:

Document(page_content, metadata)
Why this matters:
Keeps text + page info together
Helps track source of answers later
3. 🧠 Embeddings (LangChain + HuggingFace)

I use:

HuggingFaceEmbeddings
What LangChain does here:
Converts text into numerical vectors (embeddings)
Represents meaning of sentences mathematically

👉 This allows semantic search instead of keyword search

4. 🗄️ Vector Storage (FAISS via LangChain)

I use:

FAISS.from_documents()
What LangChain does:
Stores embeddings in FAISS vector database
Organizes them for fast similarity search

👉 Now my PDF is converted into a searchable knowledge base

5. 🔍 Retriever (MOST IMPORTANT PART of LangChain)
retriever.invoke(query)
What LangChain does:
Takes user question
Converts it into embedding
Finds most similar chunks from FAISS
Returns relevant document sections

👉 This is the “Retrieval” step in RAG

6. 🔗 Chain (Custom logic built on top of LangChain)

In my chains.py, I combine:

retrieved documents (LangChain output)
prompt creation
LLM response generation
So the chain does:
User Question
   ↓
LangChain Retriever (FAISS search)
   ↓
Relevant PDF chunks
   ↓
Prompt creation
   ↓
LLM generates answer
🧠 Final explanation (how to say it in interview)

👉 You can say this directly:

“In my project, I used LangChain as the backbone of a RAG system. It handles document loading using PyPDFLoader, converts text into embeddings using HuggingFaceEmbeddings, stores them in a FAISS vector database, and retrieves relevant chunks based on user queries. Then, I built a custom chain that takes these retrieved chunks, builds a prompt, and sends it to a transformer model to generate the final answer. So LangChain is responsible for the entire data pipeline from PDF ingestion to retrieval, while I control the final LLM response logic in my chain.”