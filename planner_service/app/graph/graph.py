from langgraph.graph import StateGraph, START, END
from .state import PlannerState
from .edges import route_after_intent
from .nodes import intent_node, planner_node
from app.utils import log, PlannerException

def build_graph():
    try:
        graph = StateGraph(PlannerState)

        # nodes -
        graph.add_node("intent", intent_node)
        graph.add_node("planner", planner_node)

        # edges -
        graph.add_edge(START, "intent")
        graph.add_conditional_edges(
            "intent", 
            route_after_intent,
            {
                "intent": "intent",
                "planner": "planner"
            }
        )
        graph.add_edge("planner", END)
        log.info("Graph created.")
        return graph.compile()
    
    except Exception as e:
        PlannerException(
            e, 
            context={
                "operation": "Build Graph"
            }
        )




