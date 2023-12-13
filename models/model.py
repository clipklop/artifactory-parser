import datetime
from typing import Optional

from sqlalchemy import DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql import func


class Base(DeclarativeBase):
    pass

class ArtifactStorage(Base):
    __tablename__ = "services_artifact_storage"

    id: Mapped[int] = mapped_column(primary_key=True)
    repo_key: Mapped[str]
    repo_type: Mapped[Optional[str]]
    used_space: Mapped[Optional[str]]
    package_type: Mapped[Optional[str]]
    folders_count: Mapped[Optional[int]]
    files_count: Mapped[Optional[int]]
    free_space_percentage: Mapped[Optional[str]]
    date_added: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    
    def __repr__(self) -> str:
        return f"ArtifactStorage(id={self.id!r}, repo_key={self.repo_key!r}, used_space={self.used_space!r})"
