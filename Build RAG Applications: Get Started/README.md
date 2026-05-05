# PDF RAG Assistant

A simple **Retrieval-Augmented Generation (RAG)** project built using **Python, LangChain, ChromaDB, HuggingFace embeddings, and an LLM**.

This project allows you to load a PDF document, convert it into embeddings, store vectors in a persistent database, and ask natural language questions about the content.

---

## Features

* Load PDF documents as knowledge source
* Split large documents into chunks
* Generate embeddings using Sentence Transformers
* Store vectors in ChromaDB
* Ask questions in chat mode
* Retrieve relevant chunks before generating answers
* Persistent vector database (no need to re-embed every run)

---

## Tech Stack

* Python
* LangChain
* ChromaDB
* HuggingFace Embeddings
* OpenAI-compatible LLM endpoint (GitHub Models)

---

## Project Structure

```text
project/
│── ingest.py        # Load PDF and create vector database
│── chat.py          # Ask questions from terminal
│── dsa-python.pdf   # Source PDF
│── chroma_db/       # Persistent vector database
│── requirements.txt
```

---

## Installation

Create virtual environment:

```bash
python3 -m venv myenv
source myenv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install langchain langchain-openai langchain-community langchain-huggingface langchain-chroma chromadb pypdf
```

---

## Environment Variables

Set your GitHub Models token:

```bash
export GITHUB_TOKEN=your_token_here
```

---

## Step 1: Create Vector Database

Run once:

```bash
python3 ingest.py
```

This will:

* Load the PDF
* Split into chunks
* Generate embeddings
* Save vectors to ChromaDB

---

## Step 2: Start Chat

```bash
python3 chat.py
```

Example:

```text
Ask Question: What is binary search?

Answer:
Binary search is a classic algorithm...
```

---

## Author

Rishit Dwivedi

---

