from asyncio.log import logger

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
import os
from dotenv import load_dotenv
from langchain_community.embeddings import FakeEmbeddings

load_dotenv()

# Load code files (for now, just one file)

import os
from langchain_community.document_loaders import TextLoader

def load_documents():
    documents = []

    repo_path = "repo"

    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py"):  # only load python files
                file_path = os.path.join(root, file)
                try:
                    loader = TextLoader(file_path, encoding="utf-8")
                    documents.extend(loader.load())
                except:
                    pass  # skip problematic files

    return documents


# Split into chunks

def split_documents(documents):
    splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
    )
    return splitter.split_documents(documents)

# Create vector DB

def create_vector_store(chunks):
    embeddings = FakeEmbeddings(size=1536)
    db = FAISS.from_documents(chunks, embeddings)
    return db

# Main RAG pipeline

def setup_rag():
    docs = load_documents()
    chunks = split_documents(docs)
    db = create_vector_store(chunks)
    return db

# Query RAG

def query_rag(db, query):
    logger.info(f"Searching for query: {query}")
    docs = db.similarity_search(query, k=3)
    context = "\n".join([doc.page_content for doc in docs])
    logger.info(f"Retrieved {len(docs)} documents")
    return context
