import asyncio

import aiohttp
import requests

urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        'https://ru.wikipedia.org/',
        'https://ru.hexlet.io/',
        'https://megaseller.shop/',
        'https://linux.org',
        'https://metanit.com/',
        ]


async def parser_url(url: str, name: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            with open(name, 'w', encoding='UTF-8') as file:
                r = await response.text()
                file.write(r)


if __name__ == '__main__':
    tasks = []
    for i, url in enumerate(URL_LIST):
        task = asyncio.ensure_future(parser_url(url, f'aiohttp-{i}.txt'))
        tasks.append(task)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
