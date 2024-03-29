import asyncio
import time
from aiohttp import ClientSession


async def get_full_name(repos_url, user, session):
    async with session.get(url=repos_url) as response:
        repos = await response.json()
        for repo in repos:
            full_name = repo["full_name"]
        print(f"user под именем {user} имеет полное имя репозитория {full_name}")

async def get_repos(user):
    async with ClientSession() as session:
        url = f"https://api.github.com/users/{user}"

        async with session.get(url=url) as response:
            user_json = await response.json()
            print(user_json)
            repos_url = user_json["repos_url"]
            await get_full_name(repos_url, user, session)
            
            


async def main(users):
    tasks = []
    for user in users:
        tasks.append(asyncio.create_task(get_repos(user)))

    for task in tasks:
        await task


users = [
    "Arantir1",
    "EgorTimofeychik",
    "maximax15",
    "letov2110",
    "denirix",
    "Noowkies",
    "NikDychek",
    "marinamonit",
    "PolonskyIllya",
    "temabuchka88",
    "LuydmilaKot",
    "katherinepcholka",
    "telenchenkosergey",
]


asyncio.run(main(users))
