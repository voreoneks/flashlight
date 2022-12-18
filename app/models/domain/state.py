from pydantic import BaseModel

class State(BaseModel):
    command: str
    metadata: float