import asyncio
import aiohttp
from db import add_data

URLS = ['http://whatismyip.akamai.com/', 'https://api.ipify.org/', 'https://icanhazip.com/']


async def get(session: aiohttp.ClientSession, url: str):
    async with session.get(url, ssl=False) as response:
        ip = await response.text()
        add_data(url, str(ip))


async def main(urls: list):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(get(session=session, url=url))
        htmls = await asyncio.gather(*tasks)
        return htmls


asyncio.run(main(URLS))
