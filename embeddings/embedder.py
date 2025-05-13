from langchain_ollama import OllamaEmbeddings
from langchain_core.embeddings import Embeddings
import logging
from functools import lru_cache

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to return a cached instance of the Ollama embedder
@lru_cache(maxsize=1)
def get_embedder() -> Embeddings:
    try:
        # Initialize and return the embedding model using LLaMA 3
        return OllamaEmbeddings(model="llama3")
    except Exception as e:
        logging.error(f"Failed to initialize OllamaEmbeddings: {e}")
        raise