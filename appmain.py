import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"))

print("DEBUG API KEY:", os.getenv("OPENAI_API_KEY"))