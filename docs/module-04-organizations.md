# Module 04 – Organization Management

## Objective

Develop the Organization Management API for the Distributed Job Scheduler.

Organizations act as the top-level entity of the system and own multiple projects.

---

## Features Implemented

- Create Organization
- List Organizations
- Protected API Endpoints
- JWT Authorization
- SQLAlchemy ORM Integration
- Pydantic Response Models

---

## Folder Structure

backend/
└── app/
    └── organization/
        ├── __init__.py
        ├── routes.py
        └── schemas.py

---

## Database Model

Organization

Fields

- id
- name
- description
- created_at
- updated_at

---

## API Endpoints

### Create Organization

POST /organizations/

Request

```json
{
    "name": "OpenAI",
    "description": "Distributed Job Scheduler Organization"
}
```

---

### Get Organizations

GET /organizations/

Returns all organizations stored in the database.

---

## Authentication

All organization endpoints are protected using JWT authentication.

Swagger OAuth2 authorization is enabled.

---

## Technologies Used

- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- JWT Authentication
- Pydantic

---

## Testing

Successfully verified

- Organization creation
- Organization retrieval
- Protected routes
- JWT authentication
- Response validation

---

## Status

✅ Completed