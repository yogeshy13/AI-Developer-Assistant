from http import client
from urllib import request, response
from fastapi import FastAPI
from app.api.routes import router
app = FastAPI()
app.include_router(router)
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from openai import OpenAI
from app.rag import setup_rag, query_rag
from app.services.rag_service import get_db
import ollama
# Load environment variables
import logging
from app.models import QueryRequest

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)
db = get_db()



# Health check

@app.get("/")
def read_root():
    return {"message": "AI Dev Assistant is running"}

# Basic /ask endpoint


@app.get("/health")
def health():
    return {"status": "ok"}