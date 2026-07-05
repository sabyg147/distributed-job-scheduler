from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_model import BaseModel


class RetryPolicy(BaseModel):
    __tablename__ = "retry_policies"

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True,
    )

    strategy: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )
    # fixed | linear | exponential

    max_retries: Mapped[int] = mapped_column(
        Integer,
        default=3,
    )

    initial_delay: Mapped[int] = mapped_column(
        Integer,
        default=30,
    )

    backoff_multiplier: Mapped[int] = mapped_column(
        Integer,
        default=2,
    )

    jobs = relationship(
        "Job",
        back_populates="retry_policy",
    )