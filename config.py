import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	DEBUG = False
	TESTING = False
	SECRET_KEY = '198j-1-i;lku]?a/2;lm[1]]13c09jqpzza[l0i;2lk3jrimmmlkn23lku09m1kj'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
	SQLALCHEMY_RECORD_QUERIES = True
	SQLALCHEMY_ECHO = True
	BOOTSTRAP_SERVE_LOCAL = True

class ProductionConfig(Config):
	DEBUG = False
	SQLALCHEMY_DATABASE_URI = 'mysql://missionemruser:userpass@209.208.28.247/emrdb'

class StagingConfig(Config):
	DEVELOPMENT = True
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'mysql://homewifi:homepass@209.208.28.247/emrdb'

class DevelopmentConfig(Config):
	DEVELOPMENT = True
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = 'mysql://root:rootpass@localhost/emrdb'