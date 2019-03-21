from flask import jsonify, Blueprint
from flask import request, make_response

from dao import student

blue = Blueprint('logger',  __name__)


@blue.route('/')
def query_all():

    data = student.query_all()

    def to_date(item):
        # 将age的datetime对象转成字符串
        item['age'] = item.get('age').strftime('%Y-%m-%d')
        return item

    data = list(map(to_date,  data))

    return jsonify(data)


@blue.route('/add_student/', methods=['POST'])
def add_student():
    keys = request.form.keys()
    valid_keys = ['sn', 'name', 'age', 'sex']

    for key in keys:
        if key not in valid_keys:
            return jsonify({'msg': '请填写完整的信息，请参考keys',
                            'keys': valid_keys})

    sn = request.form.get('sn')
    name = request.form.get('name')
    age = request.form.get('age')
    sex = request.form.get('sex')

    try:
        flag = student.insert(sn, name, age, sex)
    except Exception as e:
        return jsonify({'status': flag,
                        'msg': e})

    return jsonify({'status': flag})


@blue.route('/upload_log/', methods=['POST', 'PUT'])
def upload_log():

    # 获取客户端的IP
    print('remote ip: ', request.remote_addr)

    print(request.form)  # POST上传的表单数据
    print(request.args)  # GET 请求的查询参数

    # 获取上传的json数据
    json_data = request.get_json()
    print(json_data, type(json_data))

    # 获取上传文件的数据
    print(request.files)

    resp = make_response(jsonify({'code': 7000,  'msg': 'ok' }))
    resp.headers['referer'] = 'no referer'  # 跨域请求中的引用来源

    return resp