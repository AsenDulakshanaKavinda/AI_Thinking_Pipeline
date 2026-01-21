import json
from ..state import PlannerState
from .node_helper import load_prompt
from app.llm import llm

def planner_node(state: PlannerState) -> dict:
    planner_prompt = load_prompt()
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