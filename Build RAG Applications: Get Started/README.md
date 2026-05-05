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

## What Worked Well

The system answered topic-based questions such as:

* What is Binary Search?
* Explain Stacks and Queues
* What is Object-Oriented Programming?
* What is Running Time Analysis?

---

## Current Limitations

Basic RAG systems may struggle with:

* Book metadata questions (author, title)
* Full document summaries
* Table of contents extraction
* Questions requiring multiple chapter synthesis

---

## What I Learned

Building a useful RAG system is not only about using an LLM.

It also requires:

* Good chunking strategy
* Strong retrieval quality
* Metadata handling
* Better prompts
* Search system design

---

## Future Improvements

* Hybrid Search (semantic + keyword)
* Metadata extraction
* Query routing
* Better reranking
* Web UI with Streamlit / FastAPI
* Multi-document support

---

## Screenshots

(Add your terminal screenshots here)

---

## Author

Rishit Dwivedi

---

## License

MIT
