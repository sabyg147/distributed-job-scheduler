import uuid

from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_model import BaseModel


class Queue(BaseModel):
    __tablename__ = "queues"

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    priority: Mapped[int] = mapped_column(
        Integer,
        default=1,
    )

    concurrency_limit: Mapped[int] = mapped_column(
        Integer,
        default=5,
    )

    max_retries: Mapped[int] = mapped_column(
        Integer,
        default=3,
    )

    is_paused: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    project_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("projects.id", ondelete="CASCADE"),
        nullable=False,
    )

    project = relationship(
        "Project",
        back_populates="queues",
    )

    jobs = relationship(
        "Job",
        back_populates="queue",
        cascade="all, delete-orphan",
    )