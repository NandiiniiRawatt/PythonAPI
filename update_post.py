from typing import Optional
from fastapi import FastAPI, Body
from pydantic import BaseModel
from random import randrange

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

#updating posts
@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()

    # *declaring random number to id*
    post_dict['id'] = randrange(0, 100000)

    # *convert pydantic model into dictionary*
    my_posts.append(post_dict)

    # *send back the created post the array into dictionary*
    return {"data": post_dict}



