from pydantic import BaseModel
from typing import Optional


class BlogRequest(BaseModel):
    title: str
    content: str
    published: Optional[bool]
