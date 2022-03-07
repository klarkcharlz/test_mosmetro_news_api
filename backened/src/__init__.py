from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

from src.settings import DATABASE_URL

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
ma = Marshmallow(app)

from src.databases import MosmetroNews

migrate = Migrate(app, db)


from src.routes import api

from src.jobs import mosmetro_jobs
mosmetro_jobs.start()
