import pymysql
from pymysql.cursors import DictCursor

db_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db': 'stu',
    'charset': 'utf8'
}

class DB():
    def __init__(self):
        self.conn = pymysql.Connect(**db_config)

    def __enter__(self):
        return self.conn.cursor(cursor=DictCursor)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()


    def close(self):
        if self.conn:
            self.conn.close()

class AgeRangeException(Exception):
    def __init__(self):
        super().__init__('日期中年可能超出当前的时间，或者月和日超出范围')


class AgeFormatterException(Exception):
    def __init__(self):
        super().__init__('出生日期的格式不正确，参考格式： 1987-10-21')