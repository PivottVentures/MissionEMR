#!flask/bin/python
from migrate.versioning import api
from config import DevelopmentConfig

cnfg = DevelopmentConfig()
api.upgrade(cnfg.SQLALCHEMY_DATABASE_URI, cnfg.SQLALCHEMY_MIGRATE_REPO)
print 'Current database version: ' + str(api.db_version(cnfg.SQLALCHEMY_DATABASE_URI, cnfg.SQLALCHEMY_MIGRATE_REPO))