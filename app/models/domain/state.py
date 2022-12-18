from pydantic import BaseModel
from typing import Optional

class State(BaseModel):
    command: str
    metadata: Optional[float] = 1