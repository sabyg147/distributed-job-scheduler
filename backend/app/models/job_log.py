import uuid
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_model import BaseModel


class JobLog(BaseModel):
    __tablename__ = "job_logs"

    job_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("jobs.id", ondelete="CASCADE"),
        nullable=False,
    )

    level: Mapped[str] = mapped_column(
        String(20),
        default="INFO",
    )

    message: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    logged_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
    )

    job = relationship(
        "Job",
        back_populates="logs",
    )