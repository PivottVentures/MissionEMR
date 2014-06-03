from app import app, login_manager
from models import User
from forms import Patient, Login
from flask import render_template, flash, redirect, url_for#, request, session, g
from flask_login import login_user, login_required, logout_user#, current_user


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@login_manager.user_loader
def load_user(uid):
	return User.query.get(int(uid))

@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = Login()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is not None and user.check_password_hash(form.password.data):
			login_user(user)
			flash("Logged in successfully.")
			return redirect(url_for("patient"))
		else:
			return redirect(url_for('login'))
	return render_template('login.html', form=form)

@app.route('/logout', methods = ['GET'])
@login_required
def logout():
	logout_user()
	flash('You have been logged out.')
	return redirect(url_for('index'))


@app.route('/patient', methods=['GET', 'POST'])
@login_required
def patient():
    form = Patient()
    return render_template('registration.html', form=form)