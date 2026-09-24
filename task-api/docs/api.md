# API Reference

This project provides a small task management API for testing documentation monitoring. The API is intentionally simple and uses an in-memory list to store tasks.

## Base URL

The application runs locally at:

```
http://localhost:8000
```

## Endpoints

### GET /tasks
Returns all tasks currently stored in memory.

Request:

```http
GET /tasks
```

Response example:

```json
[
  {
    "id": 1,
    "title": "Learn FastAPI",
    "completed": false
  }
]
```

Behavior:
- Returns an array of task objects.
- Each task includes an `id`, `title`, and `completed` value.

### GET /tasks/{task_id}
Returns a single task by its identifier.

Request:

```http
GET /tasks/1
```

Response example:

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "completed": false
}
```

Behavior:
- Returns `404` if the task does not exist.

### POST /tasks
Creates a new task.

Request body:

```json
{
  "title": "Learn GitHub API"
}
```

Response example:

```json
{
  "id": 3,
  "title": "Learn GitHub API",
  "completed": false
}
```

Behavior:
- Adds a task with a new numeric `id`.
- The new task is created with `completed: false`.

### PUT /tasks/{task_id}
Updates an existing task.

Request body:

```json
{
  "title": "Learn FastAPI and Pydantic",
  "completed": true
}
```

Response example:

```json
{
  "id": 1,
  "title": "Learn FastAPI and Pydantic",
  "completed": true
}
```

Behavior:
- Updates the provided fields.
- Returns `404` if the task does not exist.

### DELETE /tasks/{task_id}
Deletes an existing task.

Request:

```http
DELETE /tasks/1
```

Response example:

```json
{
  "detail": "Task deleted"
}
```

Behavior:
- Removes the task from the in-memory list.
- Returns `404` if the task does not exist.

## Notes

- This API stores tasks in memory only.
- It is a simple example project intended for documentation and change monitoring tests.
