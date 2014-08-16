#import os
#basedir = os.path.abspath(os.path.dirname(__file__))

class config(object):
	DEBUG = False
	TESTING = False
	CSRF_ENABLED = True
    SECRET_KEY = '198j-1-i;lku]?a/2;lm[1]]13c09jqpzza[l0i;2lk3jrimmmlkn23lku09m1kj'
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/missiondb'   #'sqlite:///' + os.path.join(basedir, 'test.db')
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
    TESTING = Truef