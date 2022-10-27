from fastapi import Depends, FastAPI, status, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src.blog.models import Base, BlogModel, UserModel
from src.blog.schemas.requests import BlogRequest, UserRequest
from src.blog.schemas.responses import (BlogResponse, BlogDetailsResponse, UserResponse, UserDetailsResponse)
from src.utils.bcrypt_pass import bcrypt_password
from src.utils.database import engine, get_db


tags_metadata = [{"name": "blogs",
                  "description": "Manage blogs. You can list, post, read, edit or delete a blog"},
                 {"name": "users",
                  "description": ("Manage users. You can create, update or delete an user, "
                                  "you need an user for post or edit a blog")}]

app = FastAPI(title="Fast API CRUD",
              description="This is a project to listen about FastAPI and best practices",
              version="0.0.1",
              contact={"name": "João Godoi",
                       "url": "https://www.linkedin.com/in/joao-godoi/",
                       "email": "joaogodoi.dev@gmail.com"},
              openapi_tags=tags_metadata)
Base.metadata.create_all(engine)


@app.get('/blogs', response_model=List[BlogResponse], tags=['blogs'])
def list_blog(db: Session = Depends(get_db)):
    blogs = db.query(BlogModel).all()
    return blogs


@app.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=BlogDetailsResponse, tags=['blogs'])
def retrieve_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(BlogModel).get(ident=id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="blog not found, check the ID and try again!")
    return blog


@app.post('/blog', status_code=status.HTTP_201_CREATED, response_model=BlogDetailsResponse, tags=['blogs'])
def create_blog(request: BlogRequest, db: Session = Depends(get_db)):
    new_blog = BlogModel(title=request.title, content=request.content)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['blogs'])
def destroy_blog(id: int, db: Session = Depends(get_db)):
    db.query(BlogModel).filter(BlogModel.id == id).delete(synchronize_session=False)
    db.commit()
    return True


@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED,
         response_model=BlogDetailsResponse, tags=['blogs'])
def update_blog(id: int, request: BlogRequest, db: Session = Depends(get_db)):
    blog = db.query(BlogModel).filter(BlogModel.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found to update")
    blog.update({"title": request.title, "content": request.content})
    db.commit()
    return blog.first()


@app.get('/users', response_model=List[UserResponse], tags=['users'])
def list_user(db: Session = Depends(get_db)):
    blogs = db.query(UserModel).all()
    return blogs


@app.post('/user', status_code=status.HTTP_201_CREATED, response_model=UserDetailsResponse, tags=['users'])
def create_user(request: UserRequest, db: Session = Depends(get_db)):
    new_user = UserModel(first_name=request.first_name, last_name=request.last_name, email=request.email,
                         password=bcrypt_password(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get('/user/{id}', status_code=status.HTTP_200_OK, response_model=UserDetailsResponse, tags=['users'])
def retrieve_user(id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).get(ident=id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found, check the ID and try again!")
    return user


@app.delete('/user/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['users'])
def destroy_user(id: int, db: Session = Depends(get_db)):
    db.query(UserModel).filter(UserModel.id == id).delete(synchronize_session=False)
    db.commit()
    return True


@app.put('/user/{id}', status_code=status.HTTP_202_ACCEPTED,
         response_model=UserDetailsResponse, tags=['users'])
def update_uer(id: int, request: UserRequest, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found to update")
    user.update({"first_name": request.first_name, "last_name": request.last_name, "email": request.email,
                 "password": request.password})
    db.commit()
    return user.first()
