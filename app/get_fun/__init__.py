from flask import Blueprint
get_fun=Blueprint('get_fun',__name__)
from . import views,services