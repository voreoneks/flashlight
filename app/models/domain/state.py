from typing import Optional

from pydantic import BaseModel


class State(BaseModel):
    command: str
    metadata: Optional[float] = 1
