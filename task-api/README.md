# Task API

This repository is a small FastAPI project built to test a GitHub Documentation Monitor. The goal is to keep the code and documentation intentionally realistic while making it easy to introduce documentation drift.

## Purpose

The project is intentionally simple:
- It exposes a small REST API for managing tasks.
- It uses an in-memory list instead of a database.
- It includes documentation files that describe the current API behavior.
- It is designed so you can intentionally break the match between code and docs for testing.

## Installation

Create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use .venv\Scripts\activate
pip install -r requirements.txt
```

## Run the API

```bash
uvicorn app.main:app --reload
```

Then open:

```text
http://localhost:8000/docs
```

## Available endpoints

- `GET /tasks`
- `GET /tasks/{task_id}`
- `POST /tasks`
- `PUT /tasks/{task_id}`
- `DELETE /tasks/{task_id}`

## Example requests

### List tasks

```bash
curl http://localhost:8000/tasks
```

### Get one task

```bash
curl http://localhost:8000/tasks/1
```

### Create a task

```bash
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Learn GitHub API"}'
```

### Update a task

```bash
curl -X PUT http://localhost:8000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"title":"Learn FastAPI and Pydantic","completed":true}'
```

### Delete a task

```bash
curl -X DELETE http://localhost:8000/tasks/1
```

## Documentation drift test scenarios

This project is intentionally easy to break in ways that mimic stale documentation:

1. Rename an endpoint from `/tasks` to `/items` without updating docs.
2. Add a new field such as `priority` to the task object without updating docs.
3. Change `PUT /tasks/{task_id}` to `PATCH /tasks/{task_id}` without updating docs.
4. Remove or rename a field in the response model without updating docs.

These scenarios are meant to help validate whether a documentation monitor can detect code changes that no longer match the docs.
