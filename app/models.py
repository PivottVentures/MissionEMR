from . import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique = True)
	users = db.relationship('User', backref='role', lazy='dynamic')

	def __repr__(self):
		return '<Role %r>' % self.name

class User(UserMixin, db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True)
	pwhash = db.Column(db.String(128))
	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

	def __init__(self, id, username, password, role):
		self.id = id
		self.username = username
		self.set_password(password)
		self.role = role

	def set_password(self, password):
		self.pwhash = generate_password_hash(password)

	def check_password_hash(self, password):
		return check_password_hash(self.pwhash, password)

	def __repr__(self):
		return '<User %r>' % (self.username)


@login_manager.user_loader
def load_user(id):
	return User.query.get(id)


class Patient(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(255), unique=True)
	last_name = db.Column(db.String(255), unique=True)
	sex = db.Column(db.SmallInteger, default = 0)  # 0 = male, 1 = female
	age = db.Column(db.SmallInteger, default = 0)

	def __init__(self, first_name, last_name, sex, age):
		self.first_name = first_name
		self.last_name = last_name
		self.sex = sex
		self.age = age

	def __repr__(self):
		return '<Patient %r>' % self.first_name