import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GROQ_API_KEY = os.getenv("My_API_Key")
    MODEL_NAME = os.getenv("MODEL_NAME", "llama-3.3-70b-versatile")