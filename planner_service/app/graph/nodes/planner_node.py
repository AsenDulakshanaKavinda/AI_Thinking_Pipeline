import json
from ..state import PlannerState
from .node_helper import load_prompt
from app.llm import llm
from app.utils import log, PlannerException


def planner_node(state: PlannerState) -> dict:
    try:
        planner_prompt = load_prompt()
        if not planner_prompt:
            PlannerException(
                "Planner prompt is missing or empty",
                context={
                    "operation": "Planner Node"
                }
            )

        planner_prompt = (
            planner_prompt
            .replace("{{intent}}", state["intent"])
            .replace("{{user_input}}", state["user_input"])
        )
        response = llm.invoke(planner_prompt)
        result = json.load(response)
        
        return {
            "plan": result["plan"]
        }
    except Exception as e:
        PlannerException(
            e,
            context={
                "operation": "Planner Node"
            }
        )

