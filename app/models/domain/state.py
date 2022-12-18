from typing import Optional
from pydantic import Field

from pydantic import BaseModel


class State(BaseModel):
    state: str = Field(alias='command')
    color: Optional[float] = Field(None, alias='metadata')
