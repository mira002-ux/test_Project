from typing import List, Optional

from fastapi import FastAPI, HTTPException

from app.tasks import Task, TaskCreate, TaskUpdate, create_task, delete_task, get_task, list_tasks, update_task

app = FastAPI(title="Task API", version="1.0.0")


@app.get("/items", response_model=List[Task])
def get_tasks():
    return list_tasks()


@app.get("/tasks/{task_id}", response_model=Task)
def get_single_task(task_id: int):
    task = get_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.post("/tasks", response_model=Task, status_code=201)
def create_new_task(task: TaskCreate):
    return create_task(task)


@app.put("/tasks/{task_id}", response_model=Task)
def update_existing_task(task_id: int, task: TaskUpdate):
    updated = update_task(task_id, task)
    if updated is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated


@app.delete("/tasks/{task_id}")
def delete_existing_task(task_id: int):
    deleted = delete_task(task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"detail": "Task deleted"}
