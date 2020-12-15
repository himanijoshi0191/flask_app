from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from db_config import Config
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import ModelSchema


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
ma = Marshmallow(app)
db.init_app(app)


@app.before_first_request
def create_tables():
    from model import User
    db.create_all()
