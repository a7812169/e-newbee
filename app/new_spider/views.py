from . import new_spider
import random
from  flask import jsonify
from .service import *
from .. import *
@new_spider.route('/',methods=['GET'])
def xxx():
    data=getNews()
    if data:
        return jsonify(make_success(data=data))
    else:

        return jsonify(make_error(data=None))
@new_spider.route('/get',methods=['GET'])
def abc():
    data=getText()
    if data:
        return jsonify(make_success(data=data))
    else:
        return jsonify(make_error(data=None))
@new_spider.route('/getNEW',methods=['GET'])
def xxxx():
    data=getxxxx()
    if data:
        return jsonify(make_success(data=data))
    else:
        return jsonify(make_error(data=None))