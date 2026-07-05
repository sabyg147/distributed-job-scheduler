from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict


class OrganizationCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    description: str | None = None


class OrganizationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    name: str
    description: str | None = None