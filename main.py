<<<<<<< HEAD
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World!"}

=======
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World!"}
    print("Good")

>>>>>>> c2ece0c (Push git ignore)
