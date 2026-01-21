import json
from ..state import PlannerState
from .node_helper import load_prompt
from app.llm import llm_planner
from app.utils import log, PlannerException


def planner_node(state: PlannerState) -> PlannerState:
    try:
        planner_prompt = load_prompt(filepath="app/prompts/planner_prompt.txt")
        if not planner_prompt:
            PlannerException(
                "Planner prompt is missing or empty",
                context={
                    "operation": "Planner Node"
                }
            )
        
        intent = state.get("intent")
        if not intent:
            PlannerException(
                "intent is missing or empty",
                context={
                    "operation": "Planner Node"
                }
            ) 
        
        user_prompt = state.get("user_prompt")  
        if not user_prompt:
            PlannerException(
                "user prompt is missing or empty",
                context={
                    "operation": "Planner Node"
                }
            ) 


        planner_prompt = (
            planner_prompt
            .replace("{{intent}}", intent)
            .replace("{{user_prompt}}", user_prompt)
        )
        result = llm_planner.invoke(planner_prompt)
        state["plan"] = result
        return state

    except Exception as e:
        PlannerException(
            e,
            context={
                "operation": "Planner Node"
            }
        )

