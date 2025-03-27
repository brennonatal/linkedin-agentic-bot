from typing import Optional

from pydantic import BaseModel


class State(BaseModel):
    topic: Optional[str] = ""
    plan: Optional[str] = ""
    draft: Optional[str] = ""
    final: Optional[str] = ""
