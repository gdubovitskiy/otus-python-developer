"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
from pprint import pprint

import aiohttp
import asyncio

from config import BASE_DATA_URL

USERS_DATA_URL = BASE_DATA_URL + "/users"
POSTS_DATA_URL = BASE_DATA_URL + "/posts"


async def fetch_json(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def fetch_users_data(url: str = USERS_DATA_URL) -> dict:
    response: dict = await fetch_json(url)
    return response


async def fetch_posts_data(url: str = POSTS_DATA_URL) -> dict:
    response: dict = await fetch_json(url)
    return response
