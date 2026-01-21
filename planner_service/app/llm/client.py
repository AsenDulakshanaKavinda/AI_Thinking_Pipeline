
from app.utils import log, PlannerException
from langchain_mistralai import ChatMistralAI


try:
    llm = ChatMistralAI(
        model_name='mistral-small-latest',
        temperature=0.2
    )
    log.info("LLM model loaded.")
except Exception as e:
    PlannerException(
        e,
        context={
            "operation": "LLM Load."
        }
    )
    

