from app import app, login_manager, db
from models import  Test_Patient#, User, Patient, Visit, Pharmacy, Payment, Status
from forms import Patients, Login, Registration_Search, New_Patient#, Date_Range, Contact, Payment, Background, Vitals, Exam, Pharmacy
from flask import render_template, flash, redirect, url_for, request#, session, g
from flask_login import login_user, login_required, logout_user#, current_user

todays_patients=[]

### Login Views ###

@login_manager.user_loader
def load_user(uid):
	return User.query.get(int(uid))

@app.route('/')
@app.route('/index')
@app.route('/login', methods = ['GET', 'POST'])
def login():
	#form = Login(csrf_enabled=False)
	form = Login()
	if form.validate_on_submit():
		# user = User.query.filter_by(username=form.username.data).first()
		# if user is not None and user.check_password_hash(form.password.data):
		# 	login_user(user)
		# 	flash("Logged in successfully.")
		# 	return redirect(url_for("home"))
		# else:
		# 	flash("Logging in NOT SUCCESSFUL.")
		return redirect(url_for('home'))
	return render_template('login.html', form=form)

@app.route('/logout', methods = ['GET'])
#@login_required
def logout():
	logout_user()
	flash('You have been logged out.')
	return redirect(url_for('index'))


### Testing Views ###

@app.route('/test_input', methods=['GET', 'POST'])
#@login_required
def test_input():
	form = Patients()
	if request.form.get('cancel'):
		return redirect(url_for('test_output'))
	if form.validate_on_submit():
		patient = Test_Patient(first_name=form.first_name.data.title(), last_name=form.last_name.data.title(), 
			age=form.age.data, gender=form.gender.data)
		if patient is not None:
			db.session.add(patient)
			db.session.commit()
			flash("Stored patient in the database.")
			users = Test_Patient.query.all()
			for u in users:
				print u.id,u.first_name,u.last_name,u.age,u.gender
			return redirect(url_for('test_output'))
	return render_template('test_input.html', form=form)


@app.route('/test_output', methods=['GET', 'POST'])
#@login_required
def test_output():
	patients = Test_Patient.query.all()

	# for u in patients:
	# 	print u.id,u.first_name,u.last_name,u.age,u.gender
	if request.form.get('add'):
		return redirect(url_for('test_input'))

	if request.form.get('erase'):
		for pat in patients:
			db.session.delete(pat)
			db.session.commit()
		patients = []

	return render_template('test_output.html', patients=patients)

@app.route('/test_view/<patient_id>', methods=['GET', 'POST'])
#@login_required
def test_view(patient_id):
	form = Patients()
	patient = Test_Patient.query.filter_by(id=patient_id).first()
	return render_template('test_view.html', patient=patient, form=form)


@app.route('/patients_today', methods=['GET', 'POST'])
#@login_required
def patients_today():
	return render_template('patients_today.html', patients=todays_patients)


@app.route('/registration_search', methods=['GET', 'POST'])
#@login_required
def registration_search():
	form = Registration_Search()
	if form.validate_on_submit():
		print 'Validated'
		print form.criteria.data
		print form.search_term.data
		if form.criteria.data == 'first_name':
			search_results = Test_Patient.query.filter_by(first_name=form.search_term.data.title()).all()
		elif form.criteria.data == 'last_name':
			search_results = Test_Patient.query.filter_by(last_name=form.search_term.data.title()).all()
		# elif form.criteria.data == 'phone':
		# 	search_results = Test_Patient.query.filter_by(last_name=form.search_term).all()
		# elif form.criteria.data == 'address':
		# 	search_results = Test_Patient.query.filter_by(last_name=form.search_term).all()
		else:
			search_results = Test_Patient.query.filter_by(id=form.search_term.data).all()
		
		return render_template('registration_search.html', patients=search_results, form=form)

	return render_template('registration_search.html', patients=[], form=form)















### Base Views ###

@app.route('/reports', methods=['GET', 'POST'])
#@login_required
def reports():
	# Search Form
#	form = Search()
#	if form.validate_on_submit():
#		if form.search_by.data == 'first_name':
#			first_name_search = Patient.query.filter_by(first_name=form.search_term.data).all()
#		elif form.search_by.data == 'last_name':
#			last_name_search = Patient.query.filter_by(last_name=form.search_term.data).all()
#		else:
#			patient_number_search = Patient.query.filter_by(patient_number=form.search_term.data).all()
	return render_template('reports.html')#, form=form, first_name_search=first_name_search, last_name_search=last_name_search, \
#		patient_number_search=patient_number_search)

@app.route('/home', methods=['GET', 'POST'])
#@login_required
def home():

#	form = Search()
#	if form.validate_on_submit():
#		if form.search_by.data == 'first_name':
#			first_name_search = Patient.query.filter_by(first_name=form.search_term.data).all()
#		elif form.search_by.data == 'last_name':
#			last_name_search = Patient.query.filter_by(last_name=form.search_term.data).all()
#		else:
#			patient_number_search = Patient.query.filter_by(patient_number=form.search_term.data).all()
	return render_template('home.html')#, form=form, first_name_search=first_name_search, last_name_search=last_name_search, \
#		patient_number_search=patient_number_search)

@app.route('/search_results', methods=['GET', 'POST'])
#@login_required
def search_results():
#	form = Search()
#	if form.validate_on_submit():
#		if form.search_by.data == 'first_name':
#			first_name_search = Patient.query.filter_by(first_name=form.search_term.data).all()
#		elif form.search_by.data == 'last_name':
#			last_name_search = Patient.query.filter_by(last_name=form.search_term.data).all()
#		else:
#			patient_number_search = Patient.query.filter_by(patient_number=form.search_term.data).all()
	return render_template('search_results.html')#, form=form, first_name_search=first_name_search, \
#		last_name_search=last_name_search, patient_number_search=patient_number_search)


@app.route('/master', methods=['GET', 'POST'])
#@login_required
def master():

	return render_template('master.html')


### Registration Views ###  

@app.route('/registration_initial', methods=['GET', 'POST'])
#@login_required
def registration_initial():
#	form = Search()
#	if form.validate_on_submit():
#		if form.search_by.data == 'first_name':
#			first_name_search = Patient.query.filter_by(first_name=form.search_term.data).all()
#		elif form.search_by.data == 'last_name':
#			last_name_search = Patient.query.filter_by(last_name=form.search_term.data).all()
#		else:
#			patient_number_search = Patient.query.filter_by(patient_number=form.search_term.data).all()
	return render_template('registration_initial.html')#, form=form, first_name_search=first_name_search, \
#		last_name_search=last_name_search, patient_number_search=patient_number_search)


@app.route('/registration_add_new', methods=['GET', 'POST'])
#@login_required
def registration_add_new():
	form = New_Patient()
	print form.validate_on_submit()
	print form.errors
	if form.validate_on_submit():
		new_patient = New_Patient(last_name=form.last_name.data, first_name=form.first_name.data, 
			birth_date=form.birth_date.data, gender=form.gender.data, children_count=form.children_count.data, 
			address=form.address.data, phone=form.phone.data, occupation=form.occupation.data, 
			mother_name=form.mother_name.data, guardian=form.guardian.data, relation=form.relation.data)
		if new_patient is not None:
			db.session.add(new_patient)
	   		db.session.commit()
    		flash("Nouveau patient stockees dans la base de donnees. Stored new patient in the database.")
    		return render_template(url_for('registration_patient_review'))
	return render_template('registration_add_new.html', form=form)

@app.route('/registration_patient_review', methods=['GET', 'POST'])
#@login_required
def registration_patient_review():
	#form = Patients()
	#last_name_review = Patient.query.get(last_name).all()

	# render a patient's details that were just saved
	return render_template('registration_patient_review.html')

@app.route('/registration_payment', methods=['GET', 'POST'])
#@login_required
def registration_payment():
	return render_template('registration_payment.html')


### Triage Views ###

@app.route('/triage', methods=['GET', 'POST'])
#@login_required
def triage():
	return render_template('triage.html')

@app.route('/triage_patient_bg', methods=['GET', 'POST'])
#@login_required
def triage_patient_bg():
	return render_template('triage_patient_bg.html')

@app.route('/triage_patient_vitals', methods=['GET', 'POST'])
#@login_required
def triage_patient_vitals():
	return render_template('triage_patient_vitals.html')


### Doctor Views ###

@app.route('/doctor', methods=['GET', 'POST'])
#@login_required
def doctor():
	return render_template('doctor.html')

@app.route('/doctor_exam', methods=['GET', 'POST'])
#@login_required
def doctor_exam():
	return render_template('doctor_exam.html')


### Pharmacy Views ###

@app.route('/pharmacy', methods=['GET', 'POST'])
#@login_required
def pharmacy():
	return render_template('pharmacy.html')

@app.route('/pharmacy_prescription', methods=['GET', 'POST'])
#@login_required
def pharmacy_prescription():
	return render_template('pharmacy_prescription.html')