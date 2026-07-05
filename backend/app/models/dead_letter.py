import uuid
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_model import BaseModel


class DeadLetter(BaseModel):
    __tablename__ = "dead_letter_queue"

    job_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("jobs.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
    )

    reason: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    failed_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
    )

    job = relationship(
        "Job",
        back_populates="dead_letter",
    )