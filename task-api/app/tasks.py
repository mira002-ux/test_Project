from typing import Dict, List, Optional

from pydantic import BaseModel, Field


class Task(BaseModel):
    id: int
    title: str = Field(..., min_length=1, max_length=200)
    completed: bool = False
    priority: str = "medium"
    status: str = "new"


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    priority: str = "medium"
    status: str = "new"


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=200)
    completed: Optional[bool] = None
    priority: Optional[str] = None
    status: Optional[str] = None


TASKS: List[Task] = [
    Task(id=1, title="Learn FastAPI", completed=False, priority="high", status="in-progress"),
    Task(id=2, title="Build a demo app", completed=True, priority="low", status="done"),
]


def list_tasks() -> List[Task]:
    return [task.model_dump() for task in TASKS]


def get_task(task_id: int) -> Optional[Task]:
    for task in TASKS:
        if task.id == task_id:
            return task
    return None


def create_task(data: TaskCreate) -> Task:
    task_id = max((task.id for task in TASKS), default=0) + 1
    task = Task(id=task_id, title=data.title, completed=False, priority=data.priority)
    TASKS.append(task)
    return task


def update_task(task_id: int, data: TaskUpdate) -> Optional[Task]:
    task = get_task(task_id)
    if task is None:
        return None

    if data.title is not None:
        task.title = data.title
    if data.completed is not None:
        task.completed = data.completed
    if data.priority is not None:
        task.priority = data.priority
    return task


def delete_task(task_id: int) -> bool:
    for index, task in enumerate(TASKS):
        if task.id == task_id:
            del TASKS[index]
            return True
    return False
