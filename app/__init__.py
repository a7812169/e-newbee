from flask import Flask
from .msyql import DB
from flask.ext.bootstrap import Bootstrap
def create_app():
    app=Flask(__name__)
    app.config.from_object('config')
    bootstrap = Bootstrap(app)
    from .new_spider import new_spider
    from .control import control
    from .get_fun import get_fun
    from .qa import qa
    app.register_blueprint(new_spider,url_prefix='/news')
    app.register_blueprint(control,url_prefix='/index')
    app.register_blueprint(get_fun,url_prefix='/funs')
    app.register_blueprint(qa,url_prefix='/qa')
    return app
def get_connection():
    db = DB('120.79.154.232', 3306, 'root', '7812169', 'newbee')
    return db.getConnection()
def make_error(code=0, msg='请求失败', data=None):
    return {
        'error': {
            'code': code,
            'msg': msg,
            'data': data
        }
    }
def make_success(code=1, msg='请求成功', data=None):
    return {
        'code': code,
        'msg': msg,
        'data': data
    }