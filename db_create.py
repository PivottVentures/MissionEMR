#!flask/bin/python
from migrate.versioning import api
from config import DevelopmentConfig
from app import db
import os.path

tmp = DevelopmentConfig()

db.create_all()
if not os.path.exists(tmp.SQLALCHEMY_MIGRATE_REPO):
    api.create(tmp.SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(tmp.SQLALCHEMY_DATABASE_URI, tmp.SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(tmp.SQLALCHEMY_DATABASE_URI, tmp.SQLALCHEMY_MIGRATE_REPO, api.version(tmp.SQLALCHEMY_MIGRATE_REPO))