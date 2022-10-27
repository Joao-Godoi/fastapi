from pydantic import BaseModel
from src.blog.schemas.requests import BlogRequest


class BlogResponse(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True


class BlogDetailsResponse(BlogRequest):
    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    id: int
    first_name: str
    email: str

    class Config:
        orm_mode = True
