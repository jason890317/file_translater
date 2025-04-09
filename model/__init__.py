
from dotenv import load_dotenv
import os

# Initialize environment variables
load_dotenv()

# Global variables
gemini_api_key = os.getenv("GEMINI_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")
system_prompt = os.getenv("SYSTEM_PROMPT")

# Import functions to make them available when importing the package
from .model import gemini_prompt, openai_prompt