import uuid
from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_model import BaseModel


class WorkerHeartbeat(BaseModel):
    __tablename__ = "worker_heartbeats"

    worker_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("workers.id", ondelete="CASCADE"),
        nullable=False,
    )

    heartbeat_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
    )

    healthy: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    worker = relationship(
        "Worker",
        back_populates="heartbeats",
    )