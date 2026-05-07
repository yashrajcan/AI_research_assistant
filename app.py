import streamlit as st

st.title("📚 AI Research Assistant")
st.write("Upload a PDF and ask questions from it")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

# =========================
# STEP 1: PROCESS PDF
# =========================
if uploaded_file and st.button("Process PDF"):

    st.write("Processing PDF...")

    # save file
    file_path = "data/temp.pdf"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    # imports (kept inside for Streamlit reload safety)
    from src.loader import load_documents
    from src.embeddings import get_embeddings
    from src.vector_store import create_vector_store
    from src.retriever import get_retriever
    from src.chains import create_rag_chain

    # load docs (already chunked in loader)
    docs = load_documents(file_path)

    st.write("Creating embeddings...")
    embeddings = get_embeddings()

    st.write("Building vector database...")
    vector_db = create_vector_store(docs, embeddings)

    retriever = get_retriever(vector_db)

    qa_chain = create_rag_chain(retriever)

    # store in session
    st.session_state.qa_chain = qa_chain

    st.success("PDF processed successfully!")

# =========================
# STEP 2: ASK QUESTIONS
# =========================
if "qa_chain" in st.session_state:

    query = st.text_input("Ask a question")

    if query:
        result = st.session_state.qa_chain(query)

        st.write("### Answer:")
        st.write(result["result"])

        st.write("### Sources:")
        for doc in result["source_documents"]:
            st.write(doc.metadata)