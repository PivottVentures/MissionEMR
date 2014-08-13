import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_wtf.csrf import CsrfProtect
#from flask_openid import OpenID
#from auth import auth as auth_blueprint

## initializing ##
app = Flask(__name__)
CsrfProtect(app)
manager = Manager(app)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

## config ##

from app import views, models
app.config.from_object('config.DevelopmentConfig')

#basedir = os.path.abspath(os.path.dirname(__file__))

#app.config['SECRET_KEY'] = '198j-1-i;lku]?a/2;lm[1]]13c09jqpzza[l0i;2lk3jrimmmlkn23lku09m1kj'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
#app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
#app.config['SQLALCHEMY_MIGRATE_REPO'] = os.path.join(basedir, 'db_repository')
#app.config['SQLALCHEMY_RECORD_QUERIES'] = True
#app.config['SQLALCHEMY_ECHO'] = True
#app.config['BOOTSTRAP_SERVE_LOCAL'] = True
