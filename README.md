# 🚀 Local RAG Assistant — Graduation Project

A powerful, secure, and fully local **Retrieval-Augmented Generation (RAG)** system designed to answer questions accurately from custom documents such as PDF files.

The project runs entirely on the local machine using **Ollama** for local LLM inference and **ChromaDB** for semantic vector search, ensuring that documents and queries remain private and are not sent to external cloud AI providers.

---

## 🌟 Key Features

* 🔒 **100% Local & Private**

  * Runs entirely on the local machine.
  * Uses Ollama for local LLM inference.
  * Documents and queries are not sent to external cloud AI providers.

* 🔎 **Semantic Vector Search**

  * Uses ChromaDB for fast and efficient similarity search.
  * Retrieves the most relevant document chunks before generating an answer.

* ⚡ **FastAPI Backend**

  * High-performance REST API built with FastAPI.
  * Automatic interactive API documentation using Swagger UI.

* 💻 **Modern Frontend**

  * Clean and responsive single-page web interface.
  * Simple interface for submitting questions and viewing generated answers.

* 📚 **Source Attribution**

  * Generated answers include source metadata.
  * Tracks the original **file name** and **page number** whenever available.

* 🤖 **Local LLM Integration**

  * Uses Ollama to run models locally.
  * Supports models such as `llama3` and `llama3.2`.

---

## 🛠️ Tech Stack

| Component            | Technology            |
| -------------------- | --------------------- |
| Backend Framework    | FastAPI               |
| ASGI Server          | Uvicorn               |
| Vector Database      | ChromaDB              |
| Embeddings           | Sentence-Transformers |
| Embedding Model      | `all-MiniLM-L6-v2`    |
| LLM Engine           | Ollama                |
| LLM Model            | `llama3` / `llama3.2` |
| Frontend             | HTML5                 |
| Styling              | Tailwind CSS          |
| Frontend Logic       | Vanilla JavaScript    |
| Programming Language | Python                |

---

## 🧠 How the RAG System Works

The system follows a Retrieval-Augmented Generation pipeline:

```text
                 ┌─────────────────────┐
                 │     User Question   │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │     Embedding       │
                 │ Sentence-Transformers│
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │     ChromaDB        │
                 │  Semantic Search    │
                 └──────────┬──────────┘
                            │
                     Relevant Chunks
                            │
                            ▼
                 ┌─────────────────────┐
                 │       Ollama        │
                 │   Local LLM Model   │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   Generated Answer  │
                 │ + Source Metadata   │
                 └─────────────────────┘
```

### RAG Pipeline Steps

1. The user submits a question through the frontend.
2. The question is converted into a vector embedding using Sentence-Transformers.
3. ChromaDB performs semantic similarity search against indexed document chunks.
4. The most relevant chunks are retrieved.
5. The retrieved context is provided to the local Ollama LLM.
6. Ollama generates an answer based on the retrieved information.
7. The system returns the answer along with source information such as the file name and page number.

---

## 📂 Project Architecture

```text
rag-assistant-project/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── routes/
│   │   │       └── # API endpoints
│   │   │
│   │   ├── core/
│   │   │   └── # Configuration and application settings
│   │   │
│   │   ├── schemas/
│   │   │   └── # Pydantic validation models
│   │   │
│   │   ├── services/
│   │   │   └── # RAG pipeline and vector retrieval logic
│   │   │
│   │   └── main.py
│   │       # FastAPI application entry point
│   │
│   └── requirements.txt
│       # Python dependencies
│
├── frontend/
│   └── index.html
│       # Frontend user interface
│
├── data/
│   └── # Vector database and source documents
│
└── README.md
    # Project documentation
```

---

# ⚙️ Installation & Setup Guide

## 1. Prerequisites

Before running the project, make sure the following are installed:

### Python

Python **3.10 or higher** is required.

Check your Python version:

```bash
python --version
```

---

### Ollama

Install and run Ollama locally.

The project requires a local LLM model such as:

```text
llama3
```

or:

```text
llama3.2
```

After installing Ollama, pull your preferred model:

```bash
ollama pull llama3
```

To verify that Ollama is working:

```bash
ollama list
```

Make sure the selected model is available before starting the backend.

---

# 📥 2. Clone the Repository

Clone the project from GitHub:

```bash
git clone https://github.com/mohamedhalem558/rag-assistant-project.git
```

Navigate to the project directory:

```bash
cd rag-assistant-project
```

---

# 📦 3. Install Python Dependencies

Install all required backend dependencies using:

```bash
pip install -r backend/requirements.txt
```

If your system uses `pip3`, you can use:

```bash
pip3 install -r backend/requirements.txt
```

---

# ▶️ 4. Run the Backend Server

Start the FastAPI backend using Uvicorn:

```bash
uvicorn backend.app.main:app --reload
```

If the server starts successfully, the API will be available at:

```text
http://127.0.0.1:8000
```

---

# 📖 5. API Documentation

FastAPI automatically provides interactive API documentation.

### Swagger UI

Open:

```text
http://127.0.0.1:8000/docs
```

### ReDoc

You can also access the alternative API documentation at:

```text
http://127.0.0.1:8000/redoc
```

---

# 🌐 6. Run the Frontend

The frontend is located inside:

```text
frontend/index.html
```

You can open the file directly in your browser or serve it using a local development server.

For example, with Python:

```bash
python -m http.server 5500 --directory frontend
```

Then open:

```text
http://127.0.0.1:5500
```

Make sure the FastAPI backend is running at the same time.

---

# 🔄 System Workflow

The complete application workflow is:

```text
PDF / Documents
       │
       ▼
Document Processing
       │
       ▼
Text Chunking
       │
       ▼
Sentence-Transformers
       │
       ▼
Vector Embeddings
       │
       ▼
ChromaDB
       │
       │
       ▼
User Question
       │
       ▼
Question Embedding
       │
       ▼
Semantic Retrieval
       │
       ▼
Relevant Document Chunks
       │
       ▼
Ollama + Llama
       │
       ▼
Generated Answer
       │
       ▼
Source File + Page Number
```

---

# 🔐 Privacy & Security

One of the main goals of this project is to provide a **private local RAG environment**.

The system is designed so that:

* Documents remain on the local machine.
* Vector embeddings are stored locally.
* ChromaDB runs locally.
* LLM inference is performed locally through Ollama.
* User questions do not need to be sent to external AI APIs.
* No cloud-based LLM API is required for inference.

> **Note:** Privacy depends on the actual configuration and any external services or integrations added to the project.

---

# 🚀 Future Improvements

Potential future improvements include:

* 📄 Support for additional document formats.
* 📤 Web-based document uploading.
* 🧠 Support for multiple local LLM models.
* 🔍 Advanced hybrid search.
* 💬 Conversation history and multi-turn chat.
* 👤 User authentication and authorization.
* 📊 RAG analytics and monitoring.
* ⚡ Streaming LLM responses.
* 🗂️ Document management and indexing dashboard.
* 🌍 Multi-language document support.
* 🎯 Improved retrieval and reranking.
* 📝 Better citation and source tracking.

---

# 🧪 Development

During development, run the backend with:

```bash
uvicorn backend.app.main:app --reload
```

The `--reload` option automatically restarts the development server whenever backend source files are modified.

---

# 📌 Useful Commands

### Check Python version

```bash
python --version
```

### Install dependencies

```bash
pip install -r backend/requirements.txt
```

### Start FastAPI

```bash
uvicorn backend.app.main:app --reload
```

### Check Ollama models

```bash
ollama list
```

### Pull Llama 3

```bash
ollama pull llama3
```

### Start frontend server

```bash
python -m http.server 5500 --directory frontend
```

---

# 🔄 How to Push Latest Updates to GitHub

After making changes to the project or documentation, run:

```bash
git add .
```

Commit your changes:

```bash
git commit -m "Update project files and features"
```

Push the changes to GitHub:

```bash
git push origin main
```

---

# 📋 Quick Start

For a quick setup, run:

```bash
git clone https://github.com/mohamedhalem558/rag-assistant-project.git
cd rag-assistant-project
pip install -r backend/requirements.txt
ollama pull llama3
uvicorn backend.app.main:app --reload
```

Then open:

```text
http://127.0.0.1:8000/docs
```

For the frontend:

```bash
python -m http.server 5500 --directory frontend
```

Then open:

```text
http://127.0.0.1:5500
```

---

# 👨‍💻 Project

**Local RAG Assistant — Graduation Project**

Built using:

**FastAPI · ChromaDB · Sentence-Transformers · Ollama · Llama 3 · HTML · Tailwind CSS · JavaScript**

---
