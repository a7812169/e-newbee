from flask import Blueprint
qa=Blueprint('qa',__name__)
from . import views,services