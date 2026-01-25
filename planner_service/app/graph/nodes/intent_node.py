
import json
from app.utils import log, PlannerException
from app.llm import llm_intent
from ..state import PlannerState
from .node_helper import load_prompt


def intent_node(state: PlannerState) -> PlannerState:
    """ intent node that read user prompt and decide the intent of the prompt, add intent and confidence to the state """
    try:
        log.info(f"Detecting intent for the request: {state['request_id']}")
        intent_prompt = load_prompt(filepath="app/prompts/intent_prompt.txt")
        if not intent_prompt:
            PlannerException(
                "Planner prompt is missing or empty",
                context={
                    "operation": "Intent Node"
                }
            )
        
        user_prompt = state.get("user_prompt")
        if not user_prompt:
            PlannerException(
                "user_prompt is missing or empty",
                context={
                    "operation": "Intent Node"
                }
            )

        intent_prompt = intent_prompt.replace("{{user_prompt}}", user_prompt)
        result = llm_intent.invoke(intent_prompt)

        state["intent"] = result.intent
        state["confidence"] = result.confidence

        return state

    except Exception as e:
        PlannerException(
            e,
            context={
                "operation": "Intent Node"
            }
        )

