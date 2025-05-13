# 📚 Domain-Specific Q&A Bot using RAG

A Retrieval-Augmented Generation (RAG) chatbot for domain-specific question answering (Legal, Medical, Financial). It uses PDF ingestion, vector search (FAISS), and LLM-based contextual answering with LLaMA-3.

---

## 🧠 Tech Stack

- **LLM**: LLaMA-3 via Ollama
- **Embeddings**: `Olla`
- **Vector DB**: FAISS
- **RAG Framework**: Custom with LangChain-style logic
- **Frontend**: Streamlit

---

## 🚀 Features

- ✅ Upload and ingest domain-specific PDFs
- ✅ Chunk and embed documents into a vector store
- ✅ Query system with semantic retrieval (top-k)
- ✅ Context-aware answers from LLMs
- ✅ Transparent UI with context display
- ✅ Logs latency, retrieval accuracy, and token usage

---

## 📂 Project Structure

```bash
rag-domain-assistant/
├── data/                  # Uploaded and processed PDFs
├── embeddings/            # Embedding generation & FAISS storage
├── faiss_index            # FAISS based vector store
├── llm/                   # LLM interface and prompt handling
├── retrieval/             # Retrieval logic for RAG
├── utils/                 # Chunking, PDF loading, metrics
├── run_pipeline.py        # CLI tool to process and embed documents
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
