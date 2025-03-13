import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from pydantic import BaseModel
from apiservice import userapiservice


app = FastAPI()

origins = ["http://localhost:5173"]

#cross origin r server

app.add_middleware(CORSMiddleware, 
                allow_origins=origins, 
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"])

class Fruit(BaseModel):
    name: str
    
class Fruits(BaseModel):
    fruits: List[Fruit]

memory_db={"fruits":[]}

@app.get("/fruits", response_model=Fruits)
def get_fruuits():
    return Fruits(fruits=memory_db["fruits"])


@app.post("/fruits", response_model=Fruit)
def add_fruit(fruit: Fruit):
    memory_db["fruits"].append(fruit)
    return fruit


@app.get("/user/{username}")
def get_user(username):
    apiservice=userapiservice.UserAPiService()
    return apiservice.processusergists(username=username)
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
    



