import re
from fastapi import FastAPI


app = FastAPI()


@app.get('/blog')
def list_blog():
    return {"result": {"Blog 1": "Content of blog 1", "Blog 2": "Content of blog 2",
                       "Blog 3": "Content of blog 3"}}
