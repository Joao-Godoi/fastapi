from fastapi import Depends, FastAPI, status, HTTPException
from sqlalchemy.orm import Session
from typing import Optional

from src.blog.database import engine, get_db
from src.blog.models import Base, BlogModel
from src.blog.schemas import BlogRequest


app = FastAPI()
Base.metadata.create_all(engine)


@app.get('/blogs')
def list(db: Session = Depends(get_db)):
    blogs = db.query(BlogModel).all()
    return blogs


@app.get('/blog/{id}', status_code=status.HTTP_200_OK)
def retrieve(id: int, db: Session = Depends(get_db)):
    blog = db.query(BlogModel).get(ident=id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="blog not found, check the ID and try again!")
    return blog


@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create_blog(request: BlogRequest, db: Session = Depends(get_db)):
    new_blog = BlogModel(title=request.title, content=request.content)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return {"message": "Blog is created successfully!", "title": new_blog.title,
            "content": new_blog.content}
