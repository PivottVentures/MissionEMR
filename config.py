import os
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = '198j-1-i;lku]?a/2;lm[1]]13c09jqpzza[l0i;2lk3jrimmmlkn23lku09m1kj'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_RECORD_QUERIES = True