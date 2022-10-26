from fastapi import FastAPI
from typing import Optional

from models import Blog


app = FastAPI()


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
def create_blog(blog: Blog):
    return {"message": "Blog is created successfully!",
            "title": blog.title,
            "content": blog.content,
            "published": blog.published}
