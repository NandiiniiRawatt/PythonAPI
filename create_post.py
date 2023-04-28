from typing import Optional
from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

# *title string, content string, category, etc..*

class Post(BaseModel):
    title: str 
    content: str
    published: bool = True
    rating: Optional[int] = None

#create post
my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, 
            {"title": "favorite foods", "content": "I like pizza", "id": 2}]


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/createposts")
def create_posts(new_post: Post):
    #print(new_post.title)
    print(new_post.rating)

    # *convert pydantic model into dictionary*
    print(new_post.dict())
    return {"data": Post}



