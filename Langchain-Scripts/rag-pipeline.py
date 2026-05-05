import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore



temperature=0.7
max_token=1000
model_name= "openai/gpt-4.1-mini"
api_key=os.environ["GITHUB_TOKEN"]
model_url="https://models.github.ai/inference"

llm=ChatOpenAI(model=model_name,
           api_key=api_key,
           temperature=temperature,
           base_url=model_url,
           max_tokens=max_token,
           )

path="dsa-python.pdf"
loader=PyPDFLoader(path)
docs=loader.load()
print(len(docs))

text_splitter=RecursiveCharacterTextSplitter(chunk_size=10000,chunk_overlap=4000,add_start_index=True)
all_splits = text_splitter.split_documents(docs)

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
vector_store=InMemoryVectorStore(embeddings)

ids = vector_store.add_documents(documents=all_splits)
query = "What is THE ORDERED LIST ADT?"
docs = vector_store.similarity_search(query, k=3)
print("docs",docs)
context = "\n\n".join(doc.page_content for doc in docs)
print("context",context)
prompt = f"""
You are answering from retrieved PDF context.

If the answer is partially available, infer carefully from context.

If book metadata like title, author, chapters, table of contents appears in context, answer clearly.

If unavailable, say I don't know.

Context:
{context}

Question:
{query}
"""

response = llm.invoke(prompt)

print(response.content)
