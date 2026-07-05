import uuid
from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, JSON, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_model import BaseModel


class Job(BaseModel):
    __tablename__ = "jobs"

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    payload: Mapped[dict] = mapped_column(
        JSON,
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="queued",
    )
    # queued
    # scheduled
    # claimed
    # running
    # completed
    # failed
    # dead_letter

    priority: Mapped[int] = mapped_column(
        Integer,
        default=1,
    )

    retry_count: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    max_retries: Mapped[int] = mapped_column(
        Integer,
        default=3,
    )

    is_recurring: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    cron_expression: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    scheduled_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    started_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    queue_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("queues.id", ondelete="CASCADE"),
        nullable=False,
    )

    retry_policy_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("retry_policies.id"),
        nullable=True,
    )

    queue = relationship(
        "Queue",
        back_populates="jobs",
    )

    retry_policy = relationship(
        "RetryPolicy",
        back_populates="jobs",
    )

    executions = relationship(
        "JobExecution",
        back_populates="job",
        cascade="all, delete-orphan",
    )

    logs = relationship(
        "JobLog",
        back_populates="job",
        cascade="all, delete-orphan",
    )

    dead_letter = relationship(
        "DeadLetter",
        back_populates="job",
        uselist=False,
        cascade="all, delete-orphan",
    )