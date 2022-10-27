from fastapi import Depends, FastAPI, status, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src.utils.database import engine, get_db
from src.blog.models import Base, BlogModel, UserModel
from src.blog.schemas.requests import BlogRequest
from src.blog.schemas.responses import BlogResponse, BlogDetailsResponse, UserResponse


app = FastAPI()
Base.metadata.create_all(engine)


@app.get('/blogs', response_model=List[BlogResponse])
def list_blog(db: Session = Depends(get_db)):
    blogs = db.query(BlogModel).all()
    return blogs


@app.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=BlogDetailsResponse)
def retrieve_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(BlogModel).get(ident=id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="blog not found, check the ID and try again!")
    return blog


@app.post('/blog', status_code=status.HTTP_201_CREATED, response_model=BlogDetailsResponse)
def create_blog(request: BlogRequest, db: Session = Depends(get_db)):
    new_blog = BlogModel(title=request.title, content=request.content)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy_blog(id: int, db: Session = Depends(get_db)):
    db.query(BlogModel).filter(BlogModel.id == id).delete(synchronize_session=False)
    db.commit()
    return True


@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=BlogDetailsResponse)
def update_blog(id: int, request: BlogRequest, db: Session = Depends(get_db)):
    blog = db.query(BlogModel).filter(BlogModel.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found to update")
    blog.update({"title": request.title, "content": request.content})
    db.commit()
    return blog.first()


@app.get('/users', response_model=List[UserResponse])
def list_user(db: Session = Depends(get_db)):
    blogs = db.query(UserModel).all()
    return blogs
