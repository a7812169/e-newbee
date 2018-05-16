from .. import make_error,make_success
from . import qa
from .services import *
from flask import jsonify
@qa.route('/<int:tag>',methods=['GET'])
def index(tag):
    if get(tag):
        data=get(tag)
        return jsonify(make_success(data=data))
    else:
        return jsonify(make_error())
@qa.route('/search',methods=['POST'])
def search():
    if get_seach():
        data=get_seach()
        return jsonify(make_success(data=data))
    else:
        return jsonify(make_error())