# RAG Research Assistant

A lightweight **Retrieval-Augmented Generation (RAG)** research assistant built in Python using **FAISS**, **Sentence-Transformers**, and **Groq LLMs**. The system indexes documents locally and answers questions strictly based on retrieved context.

---

## ✨ Features

* Local document ingestion (PDF)
* Vector search using FAISS (CPU)
* Semantic embeddings via `all-MiniLM-L6-v2`
* Fast LLM inference using Groq
* CLI-based question answering
* Explicit disclaimer when answers are not clearly stated in documents

---

## 📂 Project Structure

```
rag-research-assistant/
│
├── data/
│   └── docs/            # Input documents (PDFs)
├── faiss_index/         # Saved FAISS index
├── venv/                # Virtual environment (ignored by git)
│
├── ingest.py             # Document ingestion & indexing
├── ask.py                # Interactive Q&A loop
├── groq_test.py          # Groq API connectivity test
├── prompt.py             # System + user prompt templates
├── query.py              # Retrieval + LLM logic
├── app.py                # (Optional) app entry point
│
├── requirements.txt
├── .env                  # API keys (not committed)
├── .gitignore
└── README.md
```

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/rag-research-assistant.git
cd rag-research-assistant
```

### 2. Create & activate virtual environment

```bash
python -m venv venv
venv\Scripts\Activate.ps1   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_groq_api_key_here
```

---

## 📥 Ingest Documents

Place your PDFs inside:

```
data/docs/
```

Run ingestion:

```bash
python ingest.py
```

This will create a FAISS index in `faiss_index/`.

---

## ❓ Ask Questions

Start the interactive Q&A loop:

```bash
python ask.py
```

Example:

```
Question: What problem does the document try to solve?
```

The assistant will:

* Answer **only using retrieved context**
* Add a disclaimer if the answer is inferred and not explicitly stated

Type `exit` to quit.

---

## 🧠 Design Philosophy

* **Accuracy over hallucination**
* Clear separation of ingestion, retrieval, and generation
* Minimal dependencies
* Runs fully on CPU (no Ollama / local LLM required)

---

## 🔐 Security Notes

* `.env` is ignored by git
* API keys are never committed
* GitHub authentication uses local credential manager

---

## ✅ Status

**Project is complete and production-stable as an MVP.**

Further work (optional):

* UI (Streamlit / FastAPI)
* Source citations per chunk
* Multi-document ranking

---

## 📜 License

MIT License

---

If you reached this README after setting everything up correctly — **you are done.**
