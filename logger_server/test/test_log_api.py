from unittest import TestCase

import requests
from requests import Response, Request

# 单元测试
class TestLogger(TestCase):
    def test_query(self):
        url = 'http://10.35.166.35:5000/'
        # method = get
        resp:Response = requests.get(url)

        # 断言响应状态码为200
        self.assertEqual(resp.status_code, 200)

        # 断言响应的数据类型为 json
        self.assertEqual(resp.headers.get('Content-Type'),
                          'application/json')

        data = resp.json()

        # 断言 data中包含code,且为10001
        self.assertEqual(data.get('code'), 10001)
    def test_upload(self):
        url = 'http://10.35.166.35:5000/upload_log/'

        digit = open('0_25.bmp', 'rb')

        data = {
            'msg': '这是上传的日志信息',
            'level': 'info',
            'name': 'flask-logger'
        }

        files = {
            'digit_0': digit
        }
        # 上传json数据
        # data=表单数据, json=json的数据
        # 注： files和json都是字节流上传的，所有不能同时使用
        #      指定了files，则json数据取消上传
        resp = requests.post(url, files=files)

        self.assertEqual(resp.status_code, 200)

        result = resp.json()  # 获取响应的json数据

        self.assertIsNotNone(result, '响应的数据不是json格式')
        self.assertEqual(result.get('code'), 7000)

    def test_add_student(self):
        url = 'http://10.35.166.72:5000/add_student/'
        data = {
            'sn': '1010',
            'name': 'jack',
            'age': '1984-04-34',
            'sex': '男'
        }

        resp = requests.post(url, data)
        resp_data = resp.json()

        print(resp_data)

        # 断言操作失败
        self.assertTrue(resp_data.get('status'))