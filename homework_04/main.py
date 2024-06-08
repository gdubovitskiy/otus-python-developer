"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
from pprint import pprint

from sqlalchemy.ext.asyncio import AsyncSession

from jsonplaceholder_requests import (
    fetch_users_data,
    fetch_posts_data
)
from models import (
    Base,
    Post,
    User
)
from models.db import async_session, async_engine


async def create_users(
        session: AsyncSession,
        *users: dict
) -> list[User]:
    users = [
        User(username=user['username'],
             email=user['email'],
             name=user['name'])
        for user in users
    ]
    session.add_all(users)
    print("prepared users:", users)
    await session.commit()
    print("created users:", users)
    return users


async def create_posts(
        session: AsyncSession,
        *posts: dict
) -> list[Post]:
    posts = [
        Post(user_id=post['userId'],
             title=post['title'],
             body=post['body'])
        for post in posts
    ]
    session.add_all(posts)
    print("prepared posts:", posts)
    await session.commit()
    print("created posts:", posts)
    return posts


async def async_main():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    users_data: list[dict]
    posts_data: list[dict]
    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data(),
    )

    async with async_session() as session:
        await create_users(session, *users_data)
        await create_posts(session, *posts_data)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
