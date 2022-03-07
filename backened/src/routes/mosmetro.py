from . import api

from src.resources import Mosmetro

api.add_resource(
    Mosmetro,
    '/news',
)
