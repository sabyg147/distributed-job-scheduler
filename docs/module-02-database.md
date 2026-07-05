# Module 02 – Database Layer

## Overview

In this module, the backend was connected to a PostgreSQL database and the complete database layer for the Distributed Job Scheduler was implemented.

The goal was to build a scalable relational database that supports organizations, projects, users, job queues, workers, scheduling, retries, execution tracking, logging, and dead-letter handling.

The database schema was implemented using SQLAlchemy ORM and version controlled using Alembic migrations.

---

## Features Implemented

### Database Setup

- Configured PostgreSQL as the primary database.
- Ran PostgreSQL inside Docker.
- Connected FastAPI with PostgreSQL using SQLAlchemy.
- Configured environment variables for database connectivity.

---

### SQLAlchemy ORM Models

Implemented the following database entities:

- Organization
- Project
- User
- Queue
- Job
- Retry Policy
- Worker
- Job Execution
- Job Log
- Scheduled Job
- Worker Heartbeat
- Dead Letter Queue

Each model includes:

- UUID Primary Key
- Created Timestamp
- Updated Timestamp
- Relationships
- Foreign Keys
- Cascade Delete Support

---

### Database Relationships

Implemented relational mappings including:

Organization
→ Projects

Project
→ Users
→ Queues

Queue
→ Jobs

Retry Policy
→ Jobs

Job
→ Executions
→ Logs
→ Dead Letter Entry

Worker
→ Executions
→ Heartbeats

These relationships allow the scheduler to efficiently manage jobs and worker execution history.

---

### Docker Integration

Configured PostgreSQL using Docker Compose.

Database container includes:

- PostgreSQL 16
- Persistent Docker Volume
- Exposed Port 5432

This allows the application to run consistently across development environments.

---

### Alembic Migration

Configured Alembic for schema version control.

Completed:

- Alembic initialization
- Metadata integration
- Automatic migration generation
- Initial schema migration
- Database upgrade

The initial migration successfully created every table required for the scheduler.

---

## Technologies Used

- Python 3.13
- FastAPI
- SQLAlchemy 2.x
- PostgreSQL
- Alembic
- Docker
- Docker Compose

---

## Challenges Faced

During development a database migration failed because the primary key type defined in the base model did not match the UUID foreign keys used by related tables.

Issue:

- Primary Key → VARCHAR
- Foreign Keys → UUID

Solution:

The BaseModel was updated to use PostgreSQL UUID as the primary key for every entity.

After regenerating the migration, the schema was successfully created.

This reinforced the importance of maintaining consistent data types across relational models.

---

## Learning Outcomes

Through this module I learned:

- Designing relational databases using SQLAlchemy ORM.
- Creating one-to-many relationships.
- Using UUIDs as primary keys.
- Managing schema changes using Alembic.
- Running PostgreSQL inside Docker.
- Building production-ready database models for scalable backend systems.

---

## Outcome

At the end of Module 2, the backend contains a fully functional relational database capable of supporting the complete Distributed Job Scheduler architecture.

The project now has a production-ready persistence layer that will be used by upcoming modules such as authentication, job scheduling, worker execution, monitoring, and analytics.