"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

import aiohttp
import asyncio

from configs.config import BASE_DATA_URL
from pprint import pprint

USERS_DATA_URL = BASE_DATA_URL + "/users"
POSTS_DATA_URL = BASE_DATA_URL + "/posts"


async def fetch_json(url: str) -> list[dict]:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def fetch_users_data(url: str = USERS_DATA_URL) -> list[dict]:
    response: list[dict] = await fetch_json(url)
    return response


async def fetch_posts_data(url: str = POSTS_DATA_URL) -> list[dict]:
    response: list[dict] = await fetch_json(url)
    return response


async def main():
    users_data = await fetch_users_data()
    posts_data = await fetch_posts_data()

    print('Users:')
    pprint(users_data)

    print('Posts:')
    pprint(posts_data)


if __name__ == '__main__':
    asyncio.run(main())