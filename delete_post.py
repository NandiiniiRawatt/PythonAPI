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
my_posts = [{"title": "favorite color", "content": "I like purple", "id": 1}, 
            {"title": "favorite foods", "content": "I like pizza", "id": 2}]

#method to find a post
def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p

#find index of the post to delete
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

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

#retriving individual post and finding that post
@app.get("/posts/{id}")
def get_post(id: int, response: Response):      # generate Response

    post = find_post(int(id))                   # whenever we have path parameter, always return as int.
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with this is id: {id} was NOT FOUND")
    return {"post_detail": post}

# Deleting post
@app.delete("/posts/{id}")
def delete_post(id: int):
    index = find_index_post(id)     # find the index in the array that has required ID
    
    if index == None:               # if index of such post doesn't exist
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist.")

    my_posts.pop(index)
   # return{'message': "Post has been successfully deleted."}
    return Response(status_code=status.HTTP_204_NO_CONTENT)     # better way to return statement
