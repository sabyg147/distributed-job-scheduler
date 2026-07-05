import uuid
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_model import BaseModel


class JobExecution(BaseModel):
    __tablename__ = "job_executions"

    job_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("jobs.id", ondelete="CASCADE"),
        nullable=False,
    )

    worker_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("workers.id"),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="claimed",
    )
    # claimed
    # running
    # completed
    # failed

    attempt_number: Mapped[int] = mapped_column(
        Integer,
        default=1,
    )

    started_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    finished_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    execution_time_ms: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    error_message: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    job = relationship(
        "Job",
        back_populates="executions",
    )

    worker = relationship(
        "Worker",
        back_populates="executions",
    )