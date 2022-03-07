from flask_restful import Api
from src import app

api = Api(app)

from .mosmetro import *
