from . import new_spider
from  flask import jsonify
from .service import getNews
from .. import *
@new_spider.route('/',methods=['GET'])
def xxx():
    data=getNews()
    if data:
        return jsonify(make_success(data=data))
    else:
        return jsonify(make_error(data=None))
