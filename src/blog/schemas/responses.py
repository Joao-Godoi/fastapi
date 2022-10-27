from pydantic import BaseModel
from src.blog.schemas.requests import BlogRequest, UserRequest


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


class UserDetailsResponse(BaseModel):
    first_name: str
    last_name: str
    email: str

    class Config:
        orm_mode = True
