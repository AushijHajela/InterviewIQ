from typing import TYPE_CHECKING

from sqlalchemy import Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


if TYPE_CHECKING:
    from app.models.interview import Interview


class Analytics(Base):
    __tablename__ = "analytics"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    interview_id: Mapped[int] = mapped_column(
        ForeignKey("interviews.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    metric_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    metric_value: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    interview: Mapped["Interview"] = relationship(
        back_populates="analytics",
    )