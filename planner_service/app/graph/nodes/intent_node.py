
import json
from app.utils import log, PlannerException
from app.llm import llm
from ..state import PlannerState
from .node_helper import load_prompt


def intent_node(state: PlannerState) -> dict:
    try:
        intent_prompt = load_prompt()
        intent_prompt = intent_prompt.replace("{{user_input}}", state["user_input"])

        response = llm.invoke(intent_prompt)

        result = json.loads(response)

        return {
            "intent": result["intent"],
            "intent_confidence": result["confidence"]
        }
    except Exception as e:
        PlannerException(
            e,
            context={
                "operation": "Intent Node"
            }
        )

