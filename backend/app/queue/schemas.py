from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class QueueCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    description: str | None = None
    priority: int = 1
    concurrency_limit: int = 5
    max_retries: int = 3
    project_id: UUID


class QueueResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    name: str
    description: str | None = None
    priority: int
    concurrency_limit: int
    max_retries: int
    is_paused: bool
    project_id: UUID