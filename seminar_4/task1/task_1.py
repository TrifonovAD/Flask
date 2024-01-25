# Задание №1
# 🐀 Написать программу, которая считывает список из 10 URL-
# адресов и одновременно загружает данные с каждого
# адреса.
# 🐀 После загрузки данных нужно записать их в отдельные
# файлы.
# 🐀 Используйте потоки.

from requests import get
from threading import Thread
from time import sleep, time

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

def download(url):
    response = get(url)
    filename = 'threading_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    sleep(0.1)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(response.text)

threads = []
for url in urls:
    thread = Thread(target=download, args=[url], daemon=True)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()