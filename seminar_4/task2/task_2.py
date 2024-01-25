# Задание №1
# 🐀 Написать программу, которая считывает список из 10 URL-
# адресов и одновременно загружает данные с каждого
# адреса.
# 🐀 После загрузки данных нужно записать их в отдельные
# файлы.
# 🐀 Используйте процессы.

from requests import get
from time import sleep, time
from multiprocessing import Process

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
    filename = 'proc_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    sleep(0.1)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(response.text)

procs = []

if __name__ == '__main__':
    for url in urls:
        proc = Process(target=download, args=[url], daemon=True)
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()



