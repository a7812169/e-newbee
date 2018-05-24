from flask import Blueprint
control=Blueprint('contrl',__name__,template_folder='templates')
from . import views