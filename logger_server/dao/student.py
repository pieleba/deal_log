import re
from datetime import datetime

from dao import DB, AgeRangeException, AgeFormatterException

db = DB()


def query_all():
    with db as cursor:
        cursor.execute('select * from student')
        data = list(cursor.fetchall())

    return data


def insert(sn, name, age, sex):
    """
    向Student表中插入记录
    :param sn:
    :param name:
    :param age:  格式： 必须是 yyyy-mm-dd格式
    :param sex:
    :return:
    """

    # 验证age格式
    if re.match(r'[1-9]{4}-[\d]{1，2}-[\d]{1，2}?', age):
        year, month, day = tuple(age.split('-'))

        current_date = datetime.now()
        if int(year) > current_date.year or \
            (int(month) >= 1 and int(month) <= 12) or \
            ( int(day) >= 1 and int(day) <= 31):

            print('------AgeRangeException-----')
            raise AgeRangeException()

    sql = 'insert into student(sn, name,age, sex) values(%s, %s, %s, %s)'
    with db as cursor:
        cursor.execute(sql, (sn, name, age, sex))

        # rowcount 在执行更新、插入、删除时有效，表示影响的记录行数
        flag = cursor.rowcount > 0  # True 插入成功， False插入失败

    return flag


def close():
    db.close()
