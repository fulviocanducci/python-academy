from sqlalchemy.orm import Mapped, mapped_column
from persistence.database.connection import Base
from datetime import datetime
from sqlalchemy import String
from sqlalchemy import func


class Credit(Base):
    __tablename__ = "credit"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, name="id")
    name: Mapped[str] = mapped_column(String(50), nullable=False, name="name")
    created_at: Mapped[datetime | None] = mapped_column(
        nullable=True, server_default=func.now(), name="created_at"
    )
