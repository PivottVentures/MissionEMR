# import os
# basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	DEBUG = False
	TESTING = False
	SECRET_KEY = ';lksjd;mk;askdj;g;ajsd;flkjasd'
	SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/missionemr_db'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	# SQLALCHEMY_MIGRATE_REPO = OS.PATH.JOIN
	# SQLALCHEMY_RECORD_QUERIES = True
	SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
	DEBUG = False

class StagingConfig(Config):
	DEVELOPMENT = True
	DEBUG = True

class DevelopmentConfig(Config):
	DEVELOPMENT = True
	DEBUG = True

class TestingConfig(Config):
	TESTING = True