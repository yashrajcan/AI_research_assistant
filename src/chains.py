from transformers import pipeline

def create_rag_chain(retriever):

    # LLM (Text generation model)
    generator = pipeline(
        "text2text-generation",
        model="google/flan-t5-base",
        max_new_tokens=200
    )

    def qa_chain(query):

        # 1. Retrieve relevant documents
        docs = retriever.invoke(query)

        # 2. Build clean context
        texts = []
        seen = set()

        for doc in docs:
            text = doc.page_content.strip()
            if text and text not in seen:
                texts.append(text)
                seen.add(text)

        context = "\n\n".join(texts[:3])

        print("\n===== CONTEXT SENT TO MODEL =====\n")
        print(context)

        # 3. Prompt for LLM
        prompt = f"""
Answer the question using ONLY the context below.

Context:
{context}

Question: {query}

If the answer is not in the context, say "I don't know".

Answer:
"""

        # 4. Generate response
        response = generator(prompt)[0]["generated_text"]

        return {
            "result": response,
            "source_documents": docs
        }

    return qa_chain