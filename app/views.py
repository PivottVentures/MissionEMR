from app import app, login_manager, db
from models import  Test_Patient, User, Patient#, Visit, Pharmacy, Payment, Status
from forms import Patients, Login, Registration_Search, Registration_Patient#, Date_Range, Contact, Payment, Background, Vitals, Exam, Pharmacy
from flask import render_template, flash, redirect, url_for, request, session, g
from flask_login import login_user, login_required, logout_user, current_user

todays_patients=[]


### Login Views ###

@login_manager.user_loader
def load_user(uid):
	return User.query.get(int(uid))

@app.route('/testdb')
def testdb():
	if db.session.query("1").from_statement("SELECT 1").all():
		return 'It works.'
	else:
		return 'Something is broken.'

@app.route('/')
@app.route('/index')
@app.route('/login', methods = ['GET', 'POST'])
def login():
	#form = Login(csrf_enabled=False)
	form = Login()
	if form.validate_on_submit():
		# user = User(username=form.username.data, password=form.password.data, role=3)
		# if user is not None:
		# 	db.session.add(user)
		# 	db.session.commit()
		user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
#		if user is not None and user.check_password_hash(form.password.data):
		if user is not None:
			login_user(user)
			print 'current user'
			print current_user
			flash('Logged in successfully.')
			return redirect(url_for('home'))
		else:
			flash('Logging in NOT SUCCESSFUL.')
		return redirect(url_for('login'))
	return render_template('login.html', form=form)

@app.before_request
def before_request():
	g.user = current_user

@app.route('/logout', methods = ['GET'])
@login_required
def logout():
	logout_user()
	flash('You have been logged out.')
	return redirect(url_for('login'))


### Testing Views ###

@app.route('/test_input', methods=['GET', 'POST'])
@login_required
def test_input():
	form = Patients()
	if request.form.get('cancel'):
		return redirect(url_for('test_output'))
	if form.validate_on_submit():
		patient = Test_Patient()
		patient.first_name=form.first_name.data.title()
		patient.last_name=form.last_name.data.title()
		patient.age=form.age.data
		patient.gender=form.gender.data
		if patient is not None:
			db.session.add(patient)
			db.session.commit()
			flash("Stored patient in the database.")
			users = Test_Patient.query.all()
			# for u in users:
			# 	print u.id,u.first_name,u.last_name,u.age,u.gender
			return redirect(url_for('test_output'))

	return render_template('test_input.html', form=form)


@app.route('/test_output', methods=['GET', 'POST'])
@login_required
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
@login_required
def test_view(patient_id):
	form = Patients()

	if request.form.get('add'):
		return redirect(url_for('test_input'))
	
	patient = Test_Patient.query.filter_by(id=patient_id).first()
	return render_template('test_view.html', patient=patient, form=form)


@app.route('/patients_today', methods=['GET', 'POST'])
@login_required
def patients_today():
	return render_template('patients_today.html', patients=todays_patients)


@app.route('/test_search', methods=['GET', 'POST'])
@login_required
def test_search():
	form = Registration_Search()
	if form.validate_on_submit():
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







@app.route('/patient_chart/<patient_id>', methods=['GET', 'POST'])
@login_required
def patient_chart(patient_id):

	if request.form.get('add'):
		return redirect(url_for('registration_add_new'))
	
	patient = Patient.query.filter_by(id=patient_id).first()
	return render_template('patient_chart.html', patient=patient)

@app.route('/registration_search', methods=['GET', 'POST'])
@login_required
def registration_search():
	form = Registration_Search()

	if request.form.get('add'):
		return redirect(url_for('registration_add_new'))
	
	if form.validate_on_submit():
		if form.criteria.data == 'first_name':
			search_results = Patient.query.filter_by(name_first=form.search_term.data.title()).all()
		elif form.criteria.data == 'last_name':
			search_results = Patient.query.filter_by(name_last=form.search_term.data.title()).all()
		# elif form.criteria.data == 'phone':
		# 	search_results = Test_Patient.query.filter_by(last_name=form.search_term).all()
		# elif form.criteria.data == 'address':
		# 	search_results = Test_Patient.query.filter_by(last_name=form.search_term).all()
		else:
			search_results = Patient.query.filter_by(id=form.search_term.data).all()
		
		return render_template('registration_search.html', patients=search_results, form=form)

	return render_template('registration_search.html', patients=[], form=form)

@app.route('/registration_output', methods=['GET', 'POST'])
@login_required
def registration_output():
	patients = Patient.query.all()

	# for u in patients:
	# 	print u.id,u.name_first,u.name_last,u.age,u.gender
	# if request.form.get('add'):
	# 	return redirect(url_for('test_input'))

	# if request.form.get('erase'):
	# 	for pat in patients:
	# 		db.session.delete(pat)
	# 		db.session.commit()
	# 	patients = []

	return render_template('registration_output.html', patients=patients)

@app.route('/registration_add_new', methods=['GET', 'POST'])
@login_required
def registration_add_new():
	form = Registration_Patient()

	#Navigate to different pages
	if request.form.get('back'):
		return redirect(url_for('registration_search'))

	if form.validate_on_submit() and request.form.get('save'):
		print 'Validated'
		new_patient = Patient(
			name_first = form.first_name.data.title(),
			name_last = form.last_name.data.title(),
			nickname = form.nickname.data.title(),
			birth_date = form.birth_date.data,
			age = form.age.data,
			gender = form.gender.data,
			phone = form.phone.data,
			address = form.address.data,
			references = form.references.data,
			occupation = form.occupation.data,
			children_count = form.children_count.data,
			name_mother = form.mother_name.data,
			name_caretaker = form.caretaker.data,
			relationship_caretaker = form.caretaker_relation.data,
			emergency_contact_person = form.emergency_person.data,
			emergency_contact_number = form.emergency_number.data
			)

		print 'created'
		if new_patient is not None:
			print 'not none'
			db.session.add(new_patient)
			db.session.commit()
			flash("Nouveau patient stockees dans la base de donnees. Stored new patient in the database.")
			users = Patient.query.all()
			for u in users:
				print u.id,u.name_first,u.name_last,u.age,u.gender,u.occupation
			
			return render_template('registration_output.html')
	else:
 		form.first_name.data = 'Luke'
 		form.last_name.data = 'Fenton'
 		form.birth_date.data = 4/4/1998
 		form.gender.data = 0
 		form.children_count.data = 0
 		form.address.data = 'Loveland'
 		form.phone.data = '645'
 		form.occupation.data = 'Engineer'
 		form.mother_name.data = 'Kathy'
 		form.caretaker.data = 'Pat'
 		form.caretaker_relation.data = 'Buddy'

	return render_template('registration_add_new.html', form=form)












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