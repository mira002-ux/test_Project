# Tasks

A task is a simple object used to track an item of work in the API.

## Task structure

Each task has the following fields:

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "completed": false
}
```

### Fields

- `id`: Unique numeric identifier for the task.
- `title`: Short human-readable title or description.
- `completed`: Boolean value indicating whether the task has been finished.

## Creating a task

To create a task, send a `POST` request to `/tasks` with a JSON body like:

```json
{
  "title": "Learn GitHub API"
}
```

The API creates a new task and assigns it the next available numeric `id`.

## Updating a task

To update an existing task, send a `PUT` request to `/tasks/{task_id}` with a JSON object containing one or both of these fields:

```json
{
  "title": "Learn FastAPI and Pydantic",
  "completed": true
}
```

- If `title` is provided, it replaces the existing task title.
- If `completed` is provided, it updates the completion status.

## Deleting a task

To delete a task, send a `DELETE` request to `/tasks/{task_id}`.

The task is removed from the in-memory list. If the ID does not exist, the API returns a `404` error.

## Notes

This project intentionally uses an in-memory list instead of a database so it stays easy to understand and easy to modify for testing documentation drift.
