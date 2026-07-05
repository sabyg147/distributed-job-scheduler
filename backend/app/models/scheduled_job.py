import uuid
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_model import BaseModel


class ScheduledJob(BaseModel):
    __tablename__ = "scheduled_jobs"

    job_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("jobs.id", ondelete="CASCADE"),
        nullable=False,
    )

    schedule_type: Mapped[str] = mapped_column(
        String(30),
        default="once",
    )
    # once
    # cron
    # interval

    cron_expression: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    next_run_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
    )

    job = relationship("Job")