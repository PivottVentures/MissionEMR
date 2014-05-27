from app import db

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True)
	password = db.Column(db.String(15), unique=True)

	def __init__(self, username, password):
		self.username = username
		self.password = password

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