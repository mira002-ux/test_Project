from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_tasks_returns_seed_data():
    response = client.get("/tasks")

    assert response.status_code == 200
    tasks = response.json()
    assert isinstance(tasks, list)
    assert tasks[0]["title"] == "Learn FastAPI"
    assert tasks[0]["completed"] is False


def test_get_single_task():
    response = client.get("/tasks/1")

    assert response.status_code == 200
    task = response.json()
    assert task["id"] == 1
    assert task["title"] == "Learn FastAPI"


def test_create_task():
    response = client.post("/tasks", json={"title": "Learn GitHub API"})

    assert response.status_code == 201
    task = response.json()
    assert task["title"] == "Learn GitHub API"
    assert task["completed"] is False
    assert "id" in task


def test_update_task():
    response = client.put("/tasks/1", json={"title": "Learn FastAPI and Pydantic", "completed": True})

    assert response.status_code == 200
    task = response.json()
    assert task["title"] == "Learn FastAPI and Pydantic"
    assert task["completed"] is True


def test_delete_task():
    create_response = client.post("/tasks", json={"title": "Delete me"})
    task_id = create_response.json()["id"]

    delete_response = client.delete(f"/tasks/{task_id}")

    assert delete_response.status_code == 200
    assert delete_response.json()["detail"] == "Task deleted"

    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404
