from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task API", version="0.1.0")


class TaskCreate(BaseModel):
    title: str
    done: bool = False


class Task(TaskCreate):
    id: int


tasks = [
    {"id": 1, "title": "Learn FastAPI", "done": False},
    {"id": 2, "title": "Build a REST API", "done": True},
]

# TODO: Implementar GET /tasks
# TODO: Implementar GET /tasks/{task_id}
# TODO: Implementar POST /tasks
# TODO: Implementar PUT /tasks/{task_id}
# TODO: Implementar DELETE /tasks/{task_id}
