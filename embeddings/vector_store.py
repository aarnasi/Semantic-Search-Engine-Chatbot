# Import FAISS (Facebook AI Similarity Search) for vector storage and similarity search
from langchain_community.vectorstores import FAISS

from embeddings import embedder

from utils import chunking

# Function to generate embeddings from chunked text and store them locally using FAISS
def generate_and_store_embeddings_faiss(chunked_text):
    # Split the input text into chunks using the chunking utility
    # Generate embeddings for each chunk using the provided embedder
    # Store the resulting FAISS index locally in a folder named "faiss_index"
    FAISS.from_documents(
        embedding=embedder.get_embedder(),
        documents=chunking.get_chunked_text(chunked_text)
    ).save_local("faiss_index")

# Function to load a previously saved FAISS vector store from disk
def load_vectorstore():
    # Load the FAISS index from the local "faiss_index" directory using the same embedder
    # `allow_dangerous_deserialization=True` allows loading pickled Python objects (use with caution)
    return FAISS.load_local(
        "faiss_index",
        embedder.get_embedder(),
        allow_dangerous_deserialization=True
    )