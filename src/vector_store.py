from langchain_community.vectorstores import FAISS

def create_vector_store(docs, embedding):
    vectorstore = FAISS.from_documents(docs, embedding)

    return vectorstore