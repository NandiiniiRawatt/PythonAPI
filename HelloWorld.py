from fastapi import FastAPI

app = FastAPI()

# *request Get method url: "/"*
@app.get("/")
def root():
    return {"message": "Hello World"}