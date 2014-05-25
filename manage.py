from flask import Flask, render_template, flash #, url_for, redirect, request
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField, IntegerField, RadioField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = '198j-1-i;lku]?a/2;lm[1]]13c09jqpzza[l0i;2lk3jrimmmlkn23lku09m1kj'
bootstrap = Bootstrap(app)

class Registration(Form):
	first_name = StringField('Prenom/First Name', validators=[DataRequired()])
	last_name = StringField('Nom/Last Name', validators=[DataRequired()])
	sex = RadioField('Sex/Gender', choices=[('male','Male/Male'), ('female','Femelle/Female')])
	age = IntegerField('Age/Age')
	submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
	form = Registration()
	if form.validate_on_submit():
	#if request.method == 'POST' and form.validate():
	#	patient = Patient(form.first_name.data, form.last_name.data, form.sex.data, form.age.data)
		flash('The data was passed')
		return 
	return render_template('index.html', form=form)
	
if __name__ == '__main__':
	app.run(debug=True)