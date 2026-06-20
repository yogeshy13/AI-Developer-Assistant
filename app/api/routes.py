from fastapi import APIRouter
router = APIRouter()
from app.services import llm_service, llm_service, rag_service
llm_service = llm_service.LLMService()
rag_service = rag_service.RAGService()  
from app.models import QueryRequest
import logging
logger = logging.getLogger(__name__)

from app.services.agent_service import AgentService
agent_service = AgentService()


@router.post("/ask")
def ask_question(request: QueryRequest):
        context = rag_service.retrieve_context(request.query)

        logger.info(f"Incoming query: {request.query}")
        prompt = f"""
        You are a senior engineer.

        Context:
        {context}

        Question:
        {request.query}
        """
        answer = llm_service.generate(prompt)
        return {"answer": answer}

@router.post("/fix")
def fix_code(request: QueryRequest):
    context = rag_service.retrieve_context(request.query)

    prompt = f"""
    You are a senior engineer.

    Analyze the following code and suggest fixes:

    Code:
    {context}

    Problem:
    {request.query}
    """

    answer = llm_service.generate(prompt)
    return {"fix_suggestion": answer}

@router.post("/tests")
def generate_tests(request: QueryRequest):
    context = rag_service.retrieve_context(request.query)

    prompt = f"""
    You are a senior QA engineer.

    Generate unit tests for this code:

    Code:
    {context}
    """

    answer = llm_service.generate(prompt)
    return {"tests": answer}

@router.post("/architecture")
def explain_architecture(request: QueryRequest):
    context = rag_service.retrieve_context(request.query)

    prompt = f"""
    You are a software architect.

    Explain the architecture of this code:

    Code:
    {context}
    """

    answer = llm_service.generate(prompt)
    return {"architecture": answer}

@router.post("/agent")
def run_agent(request: QueryRequest):
    result = agent_service.run(request.query)
    return {"response": result}