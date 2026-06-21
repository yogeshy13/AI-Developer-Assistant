from app.services.rag_service import RAGService
from app.services.llm_service import LLMService

class AgentService:
    def __init__(self):
        self.rag = RAGService()
        self.llm = LLMService()


def decide_action(self, query: str):
        prompt = f"""
        You are an AI engineering assistant.

        Classify the user request into one of:
        - fix
        - tests
        - architecture
        - general

        Query: {query}
        """

        return self.llm.generate(prompt).strip().lower()


def run(self, query: str):
        # Step 1: Decide action
        action = self.decide_action(query)

        # Step 2: Retrieve context
        context = self.rag.retrieve_context(query)

        # Step 3: Route based on action
        if "fix" in action:
            prompt = f"Fix this code:\n{context}"
        elif "test" in action:
            prompt = f"Write tests for:\n{context}"
        elif "architecture" in action:
            prompt = f"Explain architecture:\n{context}"
        else:
            prompt = f"Answer:\n{context}\n\nQuestion: {query}"

        # Step 4: Generate response
        return self.llm.generate(prompt)

def fix_flow(self, query, context):
    prompt = f"""
    You are a senior engineer.

    Step 1: Identify the issue
    Step 2: Explain why
    Step 3: Suggest fix

    Code:
    {context}

    Problem:
    {query}
    """
    return self.llm.generate(prompt)

def test_flow(self, query, context):
    prompt = f"""
    Generate unit tests for the following code:

    {context}
    """
    return self.llm.generate(prompt)

def architecture_flow(self, query, context):
    prompt = f"""
    Explain architecture and flow of this code:

    {context}
    """
    return self.llm.generate(prompt)

def general_flow(self, query, context):
    prompt = f"""
    Answer the question using the context:

    {context}

    Question:
    {query}
    """
    return self.llm.generate(prompt)
