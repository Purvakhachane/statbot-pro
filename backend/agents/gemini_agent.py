import os

from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise RuntimeError(
        "Missing Google API key. Set GOOGLE_API_KEY in your .env file or environment variables."
    )

def get_gemini_model():
    """
    Creates and returns Gemini model instance
    """
    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=GOOGLE_API_KEY,
        temperature=0
    )
    return model
