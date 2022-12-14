from pydantic import BaseModel


class BlogRequest(BaseModel):
    title: str
    content: str


class BlogResponse(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True


class BlogDetailsResponse(BlogRequest):
    class Config:
        orm_mode = True
