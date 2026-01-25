from typing import List, Dict, Optional
from pydantic import BaseModel, Field

# planner node schema
class PlanStep(BaseModel):
    step_id: int = Field(..., description="Execution order")
    action: str = Field(..., description="What to do")
    service: str = Field(..., description="Which service should execute this step")
    input: Dict = Field(default_factory=dict)
    expected_output: str


class PlannerResult(BaseModel):
    goal: str
    steps: List[PlanStep]
    constraints: Optional[List[str]] = []
    metadata: Dict = Field(default_factory=dict)
    

""" {
  "goal": "Design a scalable AI thinking pipeline",
  "steps": [
    {
      "step_id": 1,
      "action": "Identify core pipeline components",
      "service": "reasoning_service",
      "input": {},
      "expected_output": "List of pipeline components"
    },
    {
      "step_id": 2,
      "action": "Define communication protocol",
      "service": "architecture_service",
      "input": {
        "protocol": "gRPC"
      },
      "expected_output": "Service interaction design"
    },
    {
      "step_id": 3,
      "action": "Plan execution flow",
      "service": "planner_service",
      "input": {},
      "expected_output": "Ordered execution graph"
    }
  ],
  "constraints": [
    "Must be horizontally scalable",
    "Must support service isolation"
  ],
  "metadata": {
    "intent": "system_design",
    "confidence": 0.9
  }
} """

