#!flask/bin/python
from migrate.versioning import api
from config import DevelopmentConfig

cnfg = DevelopmentConfig()
v = api.db_version(cnfg.SQLALCHEMY_DATABASE_URI, cnfg.SQLALCHEMY_MIGRATE_REPO)
api.downgrade(cnfg.SQLALCHEMY_DATABASE_URI, cnfg.SQLALCHEMY_MIGRATE_REPO, v - 1)
print 'Current database version: ' + str(api.db_version(cnfg.SQLALCHEMY_DATABASE_URI, cnfg.SQLALCHEMY_MIGRATE_REPO))