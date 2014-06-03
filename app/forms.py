from flask_wtf import Form
from wtforms import StringField, SubmitField, IntegerField, RadioField, PasswordField
from wtforms.validators import Required, Length

class Patient(Form):
	first_name = StringField('Prenom/First Name', validators=[Required()])
	last_name = StringField('Nom/Last Name', validators=[Required()])
	sex = RadioField('Sex/Gender', choices=[(0,'Male/Male'), (1,'Femelle/Female')])
	age = IntegerField('Age/Age')
	submit = SubmitField('Submit')

class Login(Form):
	username = StringField('Username', validators=[Required(), Length(1, 64)])
	password = PasswordField('Password', validators=[Required()])
	submit = SubmitField('Log In')