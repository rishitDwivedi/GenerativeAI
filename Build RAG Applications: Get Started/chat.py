import os
from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# LLM
llm = ChatOpenAI(
    model="openai/gpt-4.1-mini",
    api_key=os.environ["GITHUB_TOKEN"],
    base_url="https://models.github.ai/inference",
    temperature=1.0,
    max_tokens=1000
)

# Embeddings (same model required)
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2"
)

# Load DB
vector_store = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

print("RAG Chat Ready (type exit)")

while True:
    query = input("\nAsk Question: ")

    if query.lower() == "exit":
        break

    docs = vector_store.similarity_search(query, k=3)

    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
Answer ONLY from given context.
If answer not found, say I don't know.

Context:
{context}

Question:
{query}
"""

    response = llm.invoke(prompt)

    print("\nAnswer:")
    print(response.content)