# Module 05 – Project Management

## Objective

Implement Project Management APIs for the Distributed Job Scheduler.

Projects belong to Organizations and act as containers for queues and jobs.

---

## Features Implemented

- Create Project
- List Projects
- Organization → Project relationship
- JWT Protected Endpoints
- SQLAlchemy ORM
- Pydantic Validation

---

## Folder Structure

backend/
└── app/
    └── project/
        ├── __init__.py
        ├── routes.py
        └── schemas.py

---

## API Endpoints

### Create Project

POST /projects/

Request

```json
{
    "name": "Distributed Job Scheduler",
    "description": "Backend Project",
    "organization_id": "<organization_uuid>"
}
```

---

### Get Projects

GET /projects/

Returns all projects.

---

## Authentication

JWT Protected

---

## Technologies

- FastAPI
- SQLAlchemy
- PostgreSQL
- JWT
- Pydantic

---

## Status

✅ Completed