import json
import multiprocessing
import time
from random import choice

import requests
from bs4 import BeautifulSoup

from my_code.db import PgConnSimpleParsing



def get_proxies():
    """Собираем весь список прокси с сайта и оставляем только https"""
    html = requests.get('https://free-proxy-list.net/').text
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find("table", {"class": "table table-striped table-bordered"}).find_all('tr')[1:]  # получаем первые 200
    proxies = []
    for tr in trs:
        tds = tr.find_all('td')
        ip = tds[0].text.strip()
        port = tds[1].text.strip()
        if 'yes' in tds[6].text.strip():
            proxy = {'schema': 'https', 'address': ip + ':' + port}
            # proxy = 'schema:https:address:{0}:{1}'.format(ip, port)
            proxies.append(proxy)
    return proxies

def insert_unique_proxies():
    """Добавляем прокси, которых еще не было в базе данных"""


def input_proxies_in_db_daemon():
    """Добавляем прокси, которых еще не было в базе данных"""
    while True:
        conn = PgConnSimpleParsing()
        proxies_from_site = get_proxies()
        today = time.strftime("%d.%m.%Y")
        for proxy in proxies_from_site:
            conn.insert_proxy(json.dumps(proxy), today)

        print("Inserted proxies from free-proxy-list.net")
        time.sleep(200)


if __name__ == '__main__':

    daemon_process = multiprocessing.Process(target=input_proxies_in_db_daemon, daemon=True)
    daemon_process.start()
    daemon_process.join()
