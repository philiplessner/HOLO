from typing import List, Optional
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class Blog(Base):
    __tablename__ = "blogs_table"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author: Mapped[str]
    date: Mapped[str]
    body: Mapped[str]
    pagecss: Mapped[Optional[str]]

    def __repr__(self) -> str:
        return f"<Blog(id={self.id}, title={self.title}, author={self.author}, date={self.date})>"