from fastapi import FastAPI
from pydantic import BaseModel


class StudentCreateSchema(BaseModel):
    first_name: str
    last_name: str


app = FastAPI()

students = []
@app.post("/students/")
async def create_item(item: StudentCreateSchema):
    students.append(item)
    return item

@app.get("/students/{id}")
async def root(id: int):
    return {"student": students[id]}
async def read_item(id: int):
    return {"item_id": id}