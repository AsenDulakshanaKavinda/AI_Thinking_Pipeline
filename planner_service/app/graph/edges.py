from typing import Literal
from .state import PlannerState
from langgraph.graph import END

from app.utils import log, PlannerException

MAX_INTENT_RETRIES = 3

# TODO:- later update this with a classification with human in loop 
def route_after_intent(state: PlannerState) -> Literal["intent", "planner"]:
    """
    Decide where to go after the intent node.
    """
    try:
        confidence = state.get("confidence", 0.0)
        if not confidence:
            PlannerException(
                "confidence is missing or empty",
                context={
                    "operation": "Planner Node"
                }
            )

        retries = state.get("intent_retry_count")
        if confidence < 0.75:
            log.info("Intent confidence negative going back to intent")
            if retries >= MAX_INTENT_RETRIES:
                log.info("Maximum retry count excited")
                return END
            return "intent"
        log.info("Intent confidence positive, going to planner")
        return "planner"

    except Exception as e:
        PlannerException(
            e,
            context={
                "operation": "Router after intent"
            }
        )




