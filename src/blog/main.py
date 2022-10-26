from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from typing import Optional

from src.blog.database import engine, get_db
from src.blog.models import Base, BlogModel
from src.blog.schemas import BlogRequest


app = FastAPI()
Base.metadata.create_all(engine)


@app.get('/blog')
def list_blog(limit: int = 10, published: bool = False, sort: Optional[str] = None):
    if published:
        return {"result": [{"Blog 1": {"Content": "Content of blog 1", "Published": "06.21.2022"}},
                           {"Blog 2": {"Content": "Content of blog 2", "Published": "06.21.2022"}}]}
    else:
        return {"result": [{"Blog 3": {"Content": "Content of blog 3", "Published": False}},
                           {"Blog 4": {"Content": "Content of blog 4", "Published": False}}]}


@app.get('/blog/{id}')
def detail_blog(id: int):
    return {f"Blog {id}": {"Content": f"Details of blog {id}"}}


@app.post('/blog')
def create_blog(request: BlogRequest, db: Session = Depends(get_db)):
    new_blog = BlogModel(title=request.title, content=request.content)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return {"message": "Blog is created successfully!", "title": new_blog.title,
            "content": new_blog.content}
