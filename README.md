# 🚀 Local RAG Assistant (Graduation Project)

A powerful, secure, and fully local **Retrieval-Augmented Generation (RAG)** pipeline designed to answer questions accurately from custom documents (PDFs) without relying on external cloud APIs for inference. Built with **FastAPI**, **ChromaDB**, **Sentence-Transformers**, and **Ollama (Llama 3)**.

---

## 🌟 Key Features

* **100% Local & Private:** Runs entirely on your local machine utilizing Ollama and local vector embeddings—no data sent to external cloud providers.
* **Vector Search with ChromaDB:** Fast and efficient semantic similarity search over pre-indexed document chunks.
* **FastAPI Backend:** High-performance RESTful API endpoints with automatic Swagger documentation.
* **Modern Frontend Interface:** Clean, responsive single-page web interface for seamless querying and source tracking.
* **Source Attribution:** Every generated answer includes exact metadata tracking (File name and Page number) for transparency.

---

## 🛠️ Tech Stack

* **Backend Framework:** FastAPI, Uvicorn
* **Vector Database:** ChromaDB (Persistent Client)
* **Embeddings:** Sentence-Transformers (`all-MiniLM-L6-v2` or configured model)
* **LLM Engine:** Ollama (`llama3` / `llama3.2`)
* **Frontend:** HTML5, Tailwind CSS, Vanilla JavaScript

---

## 📂 Project Architecture

```text
rag-assistant-project/
│
├── backend/
│   ├── app/
│   │   ├── api/routes/      # API endpoints (e.g., query route)
│   │   ├── core/            # Configuration and settings
│   │   ├── schemas/         # Pydantic data validation models
│   │   ├── services/        # RAG pipeline & vector retrieval logic
│   │   └── main.py          # FastAPI application entry point
│   └── requirements.txt     # Python dependencies
│
├── frontend/
│   └── index.html           # Modern web user interface
│
├── data/                    # Vector store database & source documents
└── README.md


Installation & Setup Guide
1. Prerequisites
Ensure you have the following installed on your machine:

Python (3.10 or higher)

Ollama running locally with your preferred model (e.g., llama3 or llama3.2).


2. Clone the Repository

git clone [https://github.com/mohamedhalem558/rag-assistant-project.git](https://github.com/mohamedhalem558/rag-assistant-project.git)
cd rag-assistant-project


3. Install Dependencies

pip install -r backend/requirements.txt

4. Run the Backend Server
Start the FastAPI server using Uvicorn:

uvicorn backend.app.main:app --reload

The API will be available at: http://127.0.0.1:8000

Interactive API Documentation (Swagger UI): http://127.0.0.1:8000/docs


How to Push Latest Updates to GitHub
If you make any changes to the code or documentation, update your repository with these commands:

git add .
git commit -m "Update project files and features"
git push origin main