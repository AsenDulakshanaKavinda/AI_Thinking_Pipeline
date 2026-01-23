from pydantic import BaseModel

class IntentResult(BaseModel):
    intent: str
    confidence: float