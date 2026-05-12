import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

PDF_PATH = "dsa-python.pdf"
DB_PATH = "chroma_db"

print("Loading PDF...")

loader = PyPDFLoader(PDF_PATH)
docs = loader.load()

print("Pages:", len(docs))

# Better chunking
splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150,
    add_start_index=True
)

chunks = splitter.split_documents(docs)

print("Chunks created:", len(chunks))

# Embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2"
)

# Save to Chroma
vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=DB_PATH
)

print("Vector DB saved successfully.")