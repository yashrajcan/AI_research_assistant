def get_retriever(vector_db):
    return vector_db.as_retriever(
        search_type="mmr",   # 🔥 better than similarity
        search_kwargs={"k": 3}
    )