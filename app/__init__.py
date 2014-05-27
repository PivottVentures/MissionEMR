from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models