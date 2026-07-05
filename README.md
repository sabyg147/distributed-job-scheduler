# Distributed Job Scheduler

A production-inspired backend system built using FastAPI that allows organizations to schedule, manage, execute and monitor distributed background jobs through configurable queues and workers.

The project demonstrates how modern task scheduling systems are designed using clean architecture, JWT authentication, PostgreSQL, SQLAlchemy and Docker.

---

## Why this project?

Most production systems execute thousands of asynchronous jobs every day.

Examples include:

• Sending emails
• Image processing
• Video transcoding
• Payment retries
• Notification delivery
• AI model inference
• Data synchronization

Instead of executing everything immediately, companies push these tasks into queues where background workers process them independently.

This project recreates that architecture in a simplified but scalable manner.

---

## Features Implemented

✔ JWT Authentication

Users can register, log in securely and receive JWT access tokens used to authorize protected API requests.

---

✔ Organization Management

Organizations act as the highest level entity inside the system.

Every project belongs to an organization.

---

✔ Project Management

Projects group related queues together.

Each project represents an independent workload.

---

✔ Queue Management

Queues define how jobs are processed.

Each queue stores:

• Priority
• Retry policy
• Concurrency limits
• Pause/Resume state

---

## Technologies

Python

FastAPI

SQLAlchemy

PostgreSQL

Alembic

JWT Authentication

Docker

Pydantic

Swagger UI

---

## Architecture

Client

↓

FastAPI REST API

↓

Authentication Layer

↓

Business Services

↓

Repositories

↓

PostgreSQL Database

↓

Workers (Upcoming)

---

## Current Progress

✔ Module 1

Project Foundation

✔ Module 2

Database Models

✔ Module 3

Authentication

✔ Module 4

Organizations

✔ Module 5

Projects

✔ Module 6

Queues

🚧 Module 7

Jobs

🚧 Module 8

Worker Engine

🚧 Module 9

Scheduler

🚧 Module 10

Monitoring

---

## Future Improvements

• Background Workers

• Redis Queue

• Celery Integration

• Cron Scheduling

• Retry Policies

• Dashboard

• Metrics

• Rate Limiting

• Docker Deployment

• CI/CD Pipeline

---

## API Preview

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## Status

Project currently under active development.
