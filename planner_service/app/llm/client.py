import os
from app.utils import log, PlannerException
from langchain_mistralai import ChatMistralAI
from .schemas import IntentResult, PlannerResult
from dotenv import load_dotenv; load_dotenv()

os.environ["MISTRAL_API_KEY"]=os.getenv("MISTRAL_API_KEY")

# - LLM
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
    
# - LLM intent - have a structures output
try:
    llm_intent = llm.with_structured_output(IntentResult)
    log.info("LLM intent model loaded.")
except Exception as e:
    PlannerException(
        e,
        context={
            "operation": "Intent LLM Load."
        }
    )
    
# - LLM planner - have a structures output
try:
    llm_planner = llm.with_structured_output(PlannerResult)
    log.info("LLM planner model loaded.")
except Exception as e:
    PlannerException(
        e,
        context={
            "operation": "Planner LLM Load."
        }
    )








