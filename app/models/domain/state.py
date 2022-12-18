from typing import Optional

from pydantic import BaseModel, Field

from app.resources.enums import Command


class State(BaseModel):
    state: Command = Field(alias="command")
    color: Optional[float] = Field(None, alias="metadata")
