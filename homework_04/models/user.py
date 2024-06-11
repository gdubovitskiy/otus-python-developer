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
)

from sqlalchemy.orm import relationship

from models.base import Base


class User(Base):
    username = Column(String(18), unique=True, nullable=False)
    name = Column(String(30), nullable=False)
    email = Column(String(50), unique=True, nullable=False)

    posts = relationship(
        "Post",
        back_populates="user",
        uselist=True,
    )
    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"username={self.username!r}, "
            f"name={self.name!r}, "
            f"email={self.email!r}"
            f")"
        )
