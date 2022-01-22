import json

import psycopg2


class PgConnSimpleParsing:
    '''Класс базы данных.
    Здесь будут прописываться функции для работы с БД'''

    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="random_info",
            user="postgres",
            password="Hrieleght2"
        )
        self.cur = self.conn.cursor()

    def close_conn(self):
        '''Закрыть соединение'''
        self.conn.close()

    def any_query(self, query):
        '''Основа любого запроса'''
        try:
            return self.cur.execute(query)
        except psycopg2.errors.UniqueViolation:
            print('Каждый прокси должен быть уникальным!')

##########################################

    def select_all_data_from_proxies(self):
        """Выбираем все данные из таблицы с проксями"""
        query = "SELECT * from random_info.public.proxies;"
        self.any_query(query)
        print('SELECT')
        return self.cur.fetchall()

    def select_proxies(self):
        """Выбираем только прокси"""
        all_data = self.select_all_data_from_proxies()
        return [proxy[2] for proxy in all_data]

    def insert_proxy(self, proxy, reg_date):
        """Помещаем в БД 1 прокси"""
        # proxie = json.dumps({'schema': 'https', 'address': '178.62.85.75:8080'})
        # reg_date = '2022-01-22'
        query = "INSERT INTO random_info.public.proxies (proxie, reg_date) VALUES ('{0}', '{1}');"\
            .format(proxy, reg_date)
        print(query)
        print('INSERT')
        self.any_query(query)
        self.conn.commit()

if __name__ == '__main__':
    conn = PgConnSimpleParsing()
    print(conn.select_all_data_from_proxies())
    print(conn.select_proxies())
    print(len(conn.select_proxies()))
