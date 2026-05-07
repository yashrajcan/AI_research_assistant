from langchain_community.document_loaders import PyPDFLoader

def load_documents(file_path):
    loader = PyPDFLoader(file_path)
    docs = loader.load()

    cleaned_docs = []

    for doc in docs:
        text = doc.page_content

        # 🔥 stronger filtering
        if text and len(text.strip()) > 100:
            cleaned_docs.append(doc)

    # debug
    for i, doc in enumerate(cleaned_docs):
        print("\n--- CLEAN PAGE ---\n")
        print(doc.page_content[:500])

    return cleaned_docs