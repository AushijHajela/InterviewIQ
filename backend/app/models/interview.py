from datetime import datetime

from sqlalchemy import (
    DateTime,
    ForeignKey,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Interview(Base):
    __tablename__ = "interviews"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    resume_id: Mapped[int | None] = mapped_column(
        ForeignKey("resumes.id", ondelete="SET NULL"),
        nullable=True,
    )

    job_id: Mapped[int | None] = mapped_column(
        ForeignKey("jobs.id", ondelete="SET NULL"),
        nullable=True,
    )

    job_role: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    mode: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="text",
    )

    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="in_progress",
    )

    start_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False,
    )

    end_time: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    user: Mapped["User"] = relationship(
        back_populates="interviews",
    )

    resume: Mapped["Resume | None"] = relationship(
        back_populates="interviews",
    )

    job: Mapped["Job | None"] = relationship(
        back_populates="interviews",
    )

    answers: Mapped[list["InterviewAnswer"]] = relationship(
        back_populates="interview",
        cascade="all, delete-orphan",
    )

    analytics: Mapped[list["Analytics"]] = relationship(
        back_populates="interview",
        cascade="all, delete-orphan",
    )