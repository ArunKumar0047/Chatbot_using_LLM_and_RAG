# components/vectorstore.py
"""
This module defines functions for initializing and configuring the vectorstore.

Author: Arunkumar
"""

from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma

def initialize_vectorstore(persist_directory: str):
    """
    Initialize and configure the vectorstore.

    Args:
        persist_directory (str): The directory path for persisting the vectorstore.

    Returns:
        VectorStore: The initialized vectorstore instance.
    """
    # Initialize the sentence transformer embeddings
    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    # Initialize the Chroma vectorstore
    vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding_function)

    return vectordb