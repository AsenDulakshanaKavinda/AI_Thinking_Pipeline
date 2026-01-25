from pydantic import BaseModel

# intent schema
class IntentResult(BaseModel):
    intent: str
    confidence: float