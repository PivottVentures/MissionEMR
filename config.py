# import os
# basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	DEBUG = False
	TESTING = False
	CSRF_ENABLED = True
	SECRET_KEY = ";AKLSJW;klajs/dmfpwmvlkj"
	SQLALCHEMY_DATABASE_URI = "mysql://wbrooks:bubbles@localhost/missiondb"   #'sqlite:///' + os.path.join(basedir, 'test.db')
    #SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    #SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
	#SQLALCHEMY_RECORD_QUERIES = True
    #SQLALCHEMY_ECHO = True

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