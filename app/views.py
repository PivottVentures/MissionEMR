from app import app, login_manager, db
from models import  Test_Patient, User, Patient#, Visit, Pharmacy, Payment, Status
from forms import Patients, Login, Registration_Search, Registration_Patient, Payment, Background, Vitals#, Date_Range, Contact, Exam, Pharmacy
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
		patient.first_name=form.name_first.data.title()
		patient.last_name=form.name_last.data.title()
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
		if form.criteria.data == 'name_first':
			search_results = Test_Patient.query.filter_by(first_name=form.search_term.data.title()).all()
		elif form.criteria.data == 'name_last':
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
		return redirect(url_for('registration_new_patient'))
	
	patient = Patient.query.filter_by(id=patient_id).first()
	return render_template('patient_chart.html', patient=patient)

### Registration Views ###

@app.route('/registration_search', methods=['GET', 'POST'])
@login_required
def registration_search():
	form = Registration_Search()

	if request.form.get('add'):
		return redirect(url_for('registration_new_patient'))
	
	if form.validate_on_submit():
		if form.criteria.data == 'name_first':
			search_results = Patient.query.filter_by(name_first=form.search_term.data.title()).all()
		elif form.criteria.data == 'name_last':
			search_results = Patient.query.filter_by(name_last=form.search_term.data.title()).all()
		# elif form.criteria.data == 'phone':
		# 	search_results = Test_Patient.query.filter_by(name_last=form.search_term).all()
		# elif form.criteria.data == 'address':
		# 	search_results = Test_Patient.query.filter_by(name_last=form.search_term).all()
		else:
			search_results = Patient.query.filter_by(id=form.search_term.data).all()
		
		return render_template('registration_search.html', patients=search_results, form=form)

	return render_template('registration_search.html', patients=[], form=form)

@app.route('/registration_output', methods=['GET', 'POST'])
@login_required
def registration_output():
	patients = Patient.query.all()
	# if request.form.get('erase'):
	# 	for pat in patients:
	# 		db.session.delete(pat)
	# 		db.session.commit()
	# 	patients = []

	return render_template('registration_output.html', patients=patients)

@app.route('/registration_new_patient', methods=['GET', 'POST'])
@login_required
def registration_new_patient():
	form = Registration_Patient()

	#Navigate to different pages
	if request.form.get('back'):
		return redirect(url_for('registration_search'))

	if form.validate_on_submit():
		new_patient = Patient(
			name_first = form.name_first.data.title(),
			name_last = form.name_last.data.title(),
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

		if new_patient is not None:
			db.session.add(new_patient)
			db.session.commit()
			users = Patient.query.all()
			
			if request.form.get('save'):
				return redirect(url_for('registration_existing_patient', patient_id=new_patient.id))
			elif request.form.get('continue'):
				return redirect(url_for('registration_output'))

	return render_template('registration_new_patient.html', form=form)

@app.route('/registration_existing_patient/<patient_id>', methods=['GET', 'POST'])
@login_required
def registration_existing_patient(patient_id):
	form = Registration_Patient()

	#Navigate to different pages
	if request.form.get('back'):
		return redirect(url_for('registration_search'))

	patient = Patient.query.filter_by(id=patient_id).first()

	if form.validate_on_submit() and (request.form.get('save') or request.form.get('continue')):
		patient.name_first = form.name_first.data.title()
		patient.name_last = form.name_last.data.title()
		patient.nickname = form.nickname.data.title()
		patient.birth_date = form.birth_date.data
		patient.age = form.age.data
		patient.gender = form.gender.data
		patient.phone = form.phone.data
		patient.address = form.address.data
		patient.references = form.references.data
		patient.occupation = form.occupation.data
		patient.children_count = form.children_count.data
		patient.name_mother = form.mother_name.data
		patient.name_caretaker = form.caretaker.data
		patient.relationship_caretaker = form.caretaker_relation.data
		patient.emergency_contact_person = form.emergency_person.data
		patient.emergency_contact_number = form.emergency_number.data
		db.session.commit()
		if request.form.get('save'):
			return render_template('registration_existing_patient.html', patient=patient, form=form)
		else:
			return redirect(url_for('registration_payment', patient_id=patient_id))

	else:
		form.name_first.data = patient.name_first
		form.name_last.data = patient.name_last
		form.nickname.data = patient.nickname
		form.birth_date.data = patient.birth_date
		form.age.data = patient.age
		form.gender.data = patient.gender
		form.phone.data = patient.phone
		form.address.data = patient.address
		form.references.data = patient.references
		form.occupation.data = patient.occupation
		form.children_count.data = patient.children_count
		form.mother_name.data = patient.name_mother
		form.caretaker.data = patient.name_caretaker
		form.caretaker_relation.data = patient.relationship_caretaker
		form.emergency_person.data = patient.emergency_contact_person
		form.emergency_number.data = patient.emergency_contact_number

	return render_template('registration_existing_patient.html', patient=patient, form=form)

@app.route('/registration_payment/<patient_id>', methods=['GET', 'POST'])
@login_required
def registration_payment(patient_id):
	form = Payment()

	if request.form.get('back'):
		return redirect(url_for('registration_existing_patient', patient_id=patient_id))

	patient = Patient.query.filter_by(id=patient_id).first()

	if form.validate_on_submit():
		
		# Store items in database
		# db.session.commit()
		
		return redirect(url_for('registration_output'))

	return render_template('registration_payment.html', patient=patient, form=form)


### Vitals Views ###

@app.route('/vitals', methods=['GET', 'POST'])
@login_required
def vitals():
	
	# Change to filter patients based on status=vitals
	patients = Patient.query.all()

	return render_template('vitals.html', patients=patients)

@app.route('/vitals_background/<patient_id>', methods=['GET', 'POST'])
@login_required
def vitals_background(patient_id):
	form = Background()

	#Navigate to different pages
	if request.form.get('back'):
		return redirect(url_for('vitals'))
	
	patient = Patient.query.filter_by(id=patient_id).first()

	if form.validate_on_submit() and (request.form.get('save') 
									or request.form.get('continue')
									or request.form.get('view')):
		patient.blood_type = form.blood_type.data
		patient.hiv = form.hiv.data
		patient.ht = form.ht.data
		patient.diabetes = form.diabetes.data
		patient.tb = form.tb.data
		patient.epilepsy = form.epilepsy.data
		patient.asthma = form.asthma.data
		patient.sickle_cell_anemia = form.sickle_cell_anemia.data
		patient.heart_condition = form.heart_condition.data
		patient.blood_transfusion = form.blood_transfusion.data
		patient.tea = form.tea.data
		patient.coffee = form.coffee.data
		patient.drugs = form.drugs.data
		patient.alcohol = form.alcohol.data
		patient.period_age_start = form.period_age_start.data
		patient.period_last_date = form.period_last_date.data
		patient.allergies = form.allergies.data
		patient.immunizations = form.immunizations.data
		patient.surgeries = form.surgeries.data
		patient.family_history = form.family_history.data
		patient.family_history_notes = form.background_notes.data
		
		db.session.commit()
		if request.form.get('view'):
			return redirect(url_for('registration_existing_patient', patient_id=patient_id))
		elif request.form.get('save'):
			return render_template('vitals_background.html', patient=patient, form=form)
		else:
			return redirect(url_for('vitals_vitals', patient_id=patient_id))

	else:
		form.blood_type.data = patient.blood_type
		form.hiv.data = patient.hiv
		form.ht.data = patient.ht
		form.diabetes.data = patient.diabetes
		form.tb.data = patient.tb
		form.epilepsy.data = patient.epilepsy
		form.asthma.data = patient.asthma
		form.sickle_cell_anemia.data = patient.sickle_cell_anemia
		form.heart_condition.data = patient.heart_condition
		form.blood_transfusion.data = patient.blood_transfusion
		form.tea.data = patient.tea
		form.coffee.data = patient.coffee
		form.drugs.data = patient.drugs
		form.alcohol.data = patient.alcohol
		if patient.gender == 1:
			form.period_age_start.data = patient.period_age_start
			form.period_last_date.data = patient.period_last_date
		form.allergies.data = patient.allergies
		form.immunizations.data = patient.immunizations
		form.surgeries.data = patient.surgeries
		form.family_history.data = patient.family_history
		form.background_notes.data = patient.family_history_notes

	return render_template('vitals_background.html', patient=patient, form=form)








	### Base Views ###

@app.route('/reports', methods=['GET', 'POST'])
#@login_required
def reports():

	return render_template('reports.html')

@app.route('/home', methods=['GET', 'POST'])
#@login_required
def home():

#	form = Search()
#	if form.validate_on_submit():
#		if form.search_by.data == 'name_first':
#			name_first_search = Patient.query.filter_by(name_first=form.search_term.data).all()
#		elif form.search_by.data == 'name_last':
#			name_last_search = Patient.query.filter_by(name_last=form.search_term.data).all()
#		else:
#			patient_number_search = Patient.query.filter_by(patient_number=form.search_term.data).all()
	return render_template('home.html')#, form=form, name_first_search=name_first_search, name_last_search=name_last_search, \
#		patient_number_search=patient_number_search)




@app.route('/master', methods=['GET', 'POST'])
#@login_required
def master():

	return render_template('master.html')



### Doctor Views ###

@app.route('/doctor', methods=['GET', 'POST'])
#@login_required
def doctor():
	return render_template('doctor.html')



### Pharmacy Views ###

@app.route('/pharmacy', methods=['GET', 'POST'])
#@login_required
def pharmacy():
	return render_template('pharmacy.html')
