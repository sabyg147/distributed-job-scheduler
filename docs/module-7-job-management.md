# Module 7 – Job Management

## Overview

Module 7 introduces the core entity of the Distributed Job Scheduler: **Jobs**.

A Job represents a unit of work submitted to the scheduler for execution. Every job belongs to a Queue and contains all the information required by a worker to execute it.

---

# Objectives

- Implement Job model
- Build REST APIs for Job Management
- Associate Jobs with Queues
- Support JSON payloads
- Store execution metadata
- Prepare the system for distributed workers

---

# Features Implemented

## Create Job

Creates a new job inside an existing queue.

### Endpoint

```
POST /jobs/
```

### Request Example

```json
{
  "name": "Send Welcome Email",
  "description": "Sends an email after user registration",
  "payload": {
    "email": "user@example.com",
    "template": "welcome"
  },
  "priority": 1,
  "max_retries": 3,
  "is_recurring": false,
  "cron_expression": null,
  "scheduled_at": null,
  "queue_id": "<QUEUE_ID>",
  "retry_policy_id": null
}
```

---

## List Jobs

Returns every job stored in the scheduler.

### Endpoint

```
GET /jobs/
```

---

## Get Job

Returns details of a single job.

### Endpoint

```
GET /jobs/{job_id}
```

---

# Job Model

| Field | Description |
|-------|-------------|
| id | Unique Job ID |
| name | Job name |
| description | Optional description |
| payload | JSON payload executed by workers |
| status | Current execution state |
| priority | Scheduling priority |
| retry_count | Number of retries |
| max_retries | Maximum retry attempts |
| is_recurring | Indicates recurring jobs |
| cron_expression | Cron schedule |
| scheduled_at | Scheduled execution time |
| started_at | Worker start time |
| completed_at | Completion timestamp |
| queue_id | Associated Queue |
| retry_policy_id | Optional Retry Policy |

---

# Job States

```
queued
↓

scheduled
↓

claimed
↓

running
↓

completed
```

Failure path

```
running
↓

failed
↓

retry

↓

dead_letter
```

---

# Database Relationships

```
Organization
      │
      ▼
Project
      │
      ▼
Queue
      │
      ▼
Job
```

Each Queue can contain multiple Jobs.

Each Job belongs to exactly one Queue.

---

# Validation

The API validates

- Queue exists
- Retry policy exists (optional)
- Payload is valid JSON
- Required fields are present

---

# Security

All endpoints require JWT Authentication.

Unauthorized requests receive

```
401 Unauthorized
```

---

# Technologies Used

- FastAPI
- SQLAlchemy ORM
- PostgreSQL
- Pydantic
- JWT Authentication
- Swagger UI

---

# Testing

The module was tested using Swagger UI.

Successfully verified

- Create Job
- Get All Jobs
- Get Job by ID
- Queue Validation
- JWT Authentication

---

# Current Progress

Completed Modules

- ✅ Module 1 – Project Setup
- ✅ Module 2 – Database Design
- ✅ Module 3 – Authentication
- ✅ Module 4 – Organization Management
- ✅ Module 5 – Project Management
- ✅ Module 6 – Queue Management
- ✅ Module 7 – Job Management

---

# Next Module

Module 8 introduces distributed workers.

Upcoming features include

- Worker Registration
- Worker Heartbeat
- Worker Status
- Job Claiming
- Worker Monitoring

These components will enable asynchronous execution of jobs across multiple worker instances.

---

# Conclusion

Module 7 establishes the central execution unit of the Distributed Job Scheduler.

Jobs are now securely created, validated, persisted in PostgreSQL, linked to queues, and exposed through RESTful APIs. This module forms the foundation for implementing distributed workers, scheduling algorithms, retry mechanisms, and execution monitoring in subsequent modules.