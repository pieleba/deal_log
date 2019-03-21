from app import app
from flask_cors import CORS

if __name__ == '__main__':
    CORS(app)  # 解决 跨域请求问题（两个服务器之间的请求）

    app.run(host='0.0.0.0', port=5000)
