import uuid

from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_model import BaseModel


class Worker(BaseModel):
    __tablename__ = "workers"

    worker_name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )

    hostname: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="idle",
    )
    # idle | busy | offline

    max_concurrency: Mapped[int] = mapped_column(
        Integer,
        default=5,
    )

    current_jobs: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    executions = relationship(
        "JobExecution",
        back_populates="worker",
    )

    heartbeats = relationship(
        "WorkerHeartbeat",
        back_populates="worker",
        cascade="all, delete-orphan",
    )