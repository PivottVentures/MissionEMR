from flask_wtf import Form
from wtforms import StringField, SubmitField, IntegerField, RadioField
from wtforms.validators import DataRequired

class Registration(Form):
	first_name = StringField('Prenom/First Name', validators=[DataRequired()])
	last_name = StringField('Nom/Last Name', validators=[DataRequired()])
	sex = RadioField('Sex/Gender', choices=[(0,'Male/Male'), (1,'Femelle/Female')])
	age = IntegerField('Age/Age')
	submit = SubmitField('Submit')