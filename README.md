# 📚 Domain-Specific Q&A Bot using RAG

A Retrieval-Augmented Generation (RAG) chatbot for domain-specific question
answering (Legal, Medical, Financial). It uses PDF ingestion, vector search
(FAISS), and LLM-based contextual answering with LLaMA-3.

---

## 🧠 Tech Stack

- **LLM**: LLaMA-3 via Ollama
- **Embeddings**: `OllamaEmbeddings`
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

## 📂 Enterprise Project Structure

```bash
Semantic_Search_Engine_Chatbot/
|-- data/                        # Uploaded and processed PDFs
|-- faiss_index/                 # Persisted FAISS index artifacts
|-- src/
|   |-- config/                  # Centralized application settings
|   |-- core/                    # Cross-cutting concerns (logging, etc.)
|   |-- ingestion/               # Document loaders and adapters
|   |-- processing/              # Text chunking and preparation logic
|   |-- embeddings/              # Embedding factories and vector stores
|   |-- retrieval/               # Semantic search retrieval layer
|   |-- llm/                     # Prompt templates and LLM service
|   `-- services/                # Orchestrated pipelines / business services
|-- run_pipeline.py              # CLI entrypoint for ingestion
|-- requirements.txt             # Python dependencies
`-- README.md                    # Project documentation
```

## 🛠 Usage

```bash
python run_pipeline.py data/raw/example_data/nke-10k-2023.pdf
```

This command initializes the enterprise pipeline, loads the PDF, chunks the
content, generates embeddings, and refreshes the FAISS vector store.

