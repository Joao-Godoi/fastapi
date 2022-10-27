from pydantic import BaseModel


class BlogRequest(BaseModel):
    title: str
    content: str


class UserRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
