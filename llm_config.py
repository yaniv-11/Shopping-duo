from langchain_google_genai import GoogleGenerativeAI
import os

def get_llm():
    
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("Please set your GOOGLE_API_KEY environment variable.")
    
    llm = GoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=api_key)
    return llm
