from flask import Flask

from .views import logger

app = Flask(__name__) # 创建Flask应用服务

app.register_blueprint(logger.blue)