import logging
import ollama


logger = logging.getLogger(__name__)

class LLMService:
    def __init__(self):
        pass

    def generate(self, prompt: str):
        try:
            response = ollama.chat(
                model="llama3",
                messages=[{"role": "user", "content": prompt}]
            )
            logger.info("LLM response generated successfully")
            return response["message"]["content"]
        except Exception as e:
            logger.error(f"LLM Error: {str(e)}")
            return {"error": "LLM failed"}