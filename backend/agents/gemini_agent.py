import os

from dotenv import load_dotenv
load_dotenv()

print("GEMINI_API_KEY =", os.getenv("GEMINI_API_KEY"))
from langchain_google_genai import ChatGoogleGenerativeAI


def get_gemini_model():
    """
    Creates and returns Gemini model instance
    """
    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=os.getenv("GEMINI_API_KEY"),
        temperature=0
    )
    return model