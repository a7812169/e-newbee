from flask import Flask
from .msyql import DB
from flask.ext.bootstrap import Bootstrap
def create_app():
    app=Flask(__name__)
    app.config.from_object('config')
    bootstrap = Bootstrap(app)
    from .new_spider import new_spider
    from .control import control
    app.register_blueprint(new_spider,url_prefix='/news')
    app.register_blueprint(control,url_prefix='/index')
    return app
def get_connection():
    db = DB('120.79.154.232', 3306, 'root', '7812169', 'newbee')
    return db.getConnection()