<<<<<<< HEAD
#import os
#basedir = os.path.abspath(os.path.dirname(__file__))
=======
# import os
# basedir = os.path.abspath(os.path.dirname(__file__))
>>>>>>> f88e3cfebbd893f212486676beb1db7ad8b22936

class Config(object):
	DEBUG = False
	TESTING = False
<<<<<<< HEAD
	CSRF_ENABLED = True
    SECRET_KEY = '198j-1-i;lku]?a/2;lm[1]]13c09jqpzza[l0i;2lk3jrimmmlkn23lku09m1kj'
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/missiondb'   #'sqlite:///' + os.path.join(basedir, 'test.db')
    #SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    #SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
	#SQLALCHEMY_RECORD_QUERIES = True
    #SQLALCHEMY_ECHO = True
=======
	SECRET_KEY = ';lksjd;mk;askdj;g;ajsd;flkjasd'
	SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/missionemr_db'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	# SQLALCHEMY_MIGRATE_REPO = OS.PATH.JOIN
	# SQLALCHEMY_RECORD_QUERIES = True
	SQLALCHEMY_ECHO = True
>>>>>>> f88e3cfebbd893f212486676beb1db7ad8b22936

class ProductionConfig(Config):
	DEBUG = False

class StagingConfig(Config):
	DEVELOPMENT = True
	DEBUG = True

class DevelopmentConfig(Config):
	DEVELOPMENT = True
	DEBUG = True

class TestingConfig(Config):
<<<<<<< HEAD
    TESTING = Truef
=======
	TESTING = True
>>>>>>> f88e3cfebbd893f212486676beb1db7ad8b22936
