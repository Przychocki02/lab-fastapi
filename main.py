from fastapi import FastAPI
from pydantic import BaseModel


class StudentCreateSchema(BaseModel):
    first_name: str
    last_name: str

class StudentUpdateSchema(BaseModel):
    name: str
    surname: str

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

@app.put("/student/{id}")
def update_student(id: int, updated_data: StudentUpdateSchema):
    if id not in students:
        raise HTTPException(status_code=404, detail="Student not found")

    # Aktualizacja imienia i nazwiska studenta
    students[id]["name"] = updated_data.name
    students[id]["surname"] = updated_data.surname

    return students[id]    
    
    
    
    