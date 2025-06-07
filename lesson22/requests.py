from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


class Person(BaseModel):
    name: str
    age: int

@app.post("/create_person")
async def create_person(person: Person):
    return{"message:" f"Person {person.name} created with age {person.age}"}
