from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class JobCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=255)
    description: str | None = None
    payload: dict
    priority: int = 1
    max_retries: int = 3
    is_recurring: bool = False
    cron_expression: str | None = None
    scheduled_at: datetime | None = None
    queue_id: UUID
    retry_policy_id: UUID | None = None


class JobResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    name: str
    description: str | None = None
    payload: dict
    status: str
    priority: int
    retry_count: int
    max_retries: int
    is_recurring: bool
    cron_expression: str | None = None
    scheduled_at: datetime | None = None
    started_at: datetime | None = None
    completed_at: datetime | None = None
    queue_id: UUID
    retry_policy_id: UUID | None = None