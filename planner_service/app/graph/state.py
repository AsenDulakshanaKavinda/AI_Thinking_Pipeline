from typing import TypedDict, Optional, List

class PlannerState(TypedDict, total=False):
    # request data
    request_id: str
    use_prompt: str

    # intent node output
    intent: Optional[str]
    intent_confidence: Optional[float]

    # planner node output
    plan: Optional[List[str]]

    # diagnostics 
    error: Optional[str]


""" {
    "request_id": "abc-123",
    "user_input": "Design a scalable AI pipeline",
    "intent": "system_design",
    "intent_confidence": 0.93,
    "plan": [
        "Identify system requirements",
        "Define service boundaries",
        "Design communication protocols",
        "Plan scalability and fault tolerance"
    ]
} """






