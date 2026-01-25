import os
from dotenv import load_dotenv; load_dotenv()
from app.utils import log, ReasoningException
from langchain_groq import ChatGroq


os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

def load_llm():
    """ Load LLM Model using in reasoning service."""
    try:
        llm = ChatGroq(
            model="qwen/qwen3-32b",
            temperature=0.2
        )
        log.info("Reasoning model loaded")

    except Exception as e:
        ReasoningException(
            e,
            context={
                "operation": "Load reasoning llm"
            }
        )



