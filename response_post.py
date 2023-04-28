from typing import Optional

# response, status, HTTPException used for responding of unknown posts
from fastapi import FastAPI, Body, Response, status, HTTPException
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

#method to find a post
def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p


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

# Latest post
@app.get("/posts/latest")
def get_latest_post():
    post = my_posts[len(my_posts)-1]
    return {"detail": post}


#retriving individual post and finding that post
@app.get("/posts/{id}")
def get_post(id: int, response: Response):      # generate Response

    post = find_post(int(id))                   # whenever we have path parameter, always return as int.
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with this is id: {id} was NOT FOUND")
    return {"post_detail": post}
