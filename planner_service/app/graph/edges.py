from typing import Literal
from .state import PlannerState

from app.utils import log, PlannerException

# TODO:- later update this with a classification with human in loop 
def route_after_intent(state: PlannerState) -> Literal["intent", "planner"]:
    """
    Decide where to go after the intent node.
    """
    try:
        confidence = state.get("intent_confidence", 0.0)
        if confidence > 0.75:
            log.info("Intent confidence positive going to planner")
            return "planner"
        log.info("Intent confidence negative, going back to intent")
        return "intent"
    except Exception as e:
        PlannerException(
            e,
            context={
                "operation": "Router after intent"
            }
        )




