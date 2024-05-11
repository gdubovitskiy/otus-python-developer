"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""
from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    Text
)
from sqlalchemy.orm import relationship

from models.base import Base


class Post(Base):
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    title = Column(String, nullable=False, default="", server_default="")
    body = Column(Text, nullable=False, default="", server_default="")

    user = relationship(
        "User",
        back_populates="posts",
        uselist=False,
    )

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"user_id={self.user_id!r}, "
            f"title={self.title!r}"
            f"body={self.body!r}"
            f")"
        )
