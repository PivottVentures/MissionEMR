from . import db#, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

ROLE_ADMIN = 0
ROLE_MANAGER = 1
ROLE_DOCTOR = 2
ROLE_NURSE = 3
#STATUS_REGISTRATION = 0
#STATUS_TRIAGE = 1
#STATUS_DOCTOR = 2
#STATUS_PARMACY = 3
#STATUS_HOLD = 4
#STATUS_COMPLETE = 5

class User(UserMixin, db.Model):
	__tablename__ = 'User'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True)
	password = db.Column(db.String(64))
#	pwhash = db.Column(db.String(128))
	role = db.Column(db.SmallInteger, default = 3) # 0 = admin, 1 = manager, 2 = doctor, 3 = nurse

	def __init__(self, username, password, role):
		self.username = username
		self.password = password
#		self.pwhash = generate_password_hash(password)
		self.role = role

	def check_password_hash(self, password):
		return check_password_hash(self.pwhash, password)

	def is_authenticated(self):
		return True
	
	def is_active(self):
		return True
	
	def is_anonymous(self):
		return False
	
	def get_id(self):
		return unicode(self.id)

	def __repr__(self):
		return '<User %r>' % self.username


class Test_Patient(db.Model):
	__tablename__ = 'Test_Patient'
	id = db.Column(db.Integer, primary_key=True)

	## Demographic Info ##
	last_name = db.Column(db.String(255))
	first_name = db.Column(db.String(255), default = '')
	age = db.Column(db.SmallInteger, default = 0)
	gender = db.Column(db.SmallInteger, default = 0)  # 0 = male, 1 = female

	# def __init__(self, last_name, first_name, age, gender):
	# 	self.id = id
	# 	self.last_name = last_name
	# 	self.first_name = first_name
	# 	self.age = age
	# 	self.gender = gender


class Patient(db.Model):
	__tablename__ = 'Patient'
	id = db.Column(db.Integer, primary_key=True)

	## Demographics ##
	name_first = db.Column(db.String(255), default = '')
	name_last = db.Column(db.String(255), default = '')
	nickname = db.Column(db.String(255), default = '')
	birth_date = db.Column(db.Date) # attributes: year, month, day
	age = db.Column(db.SmallInteger)
	gender = db.Column(db.SmallInteger) # 0 = male, 1 = female
	phone = db.Column(db.String(255), default = '')
	address = db.Column(db.String(255), default = '')
	references = db.Column(db.String(255), default = '')
	occupation = db.Column(db.String(255), default = '')
	children_count = db.Column(db.SmallInteger, default=0)
	name_mother = db.Column(db.String(255), default = '')
	name_caretaker = db.Column(db.String(255), default = '')
	relationship_caretaker = db.Column(db.String(255), default = '')
	emergency_contact_person = db.Column(db.String(255), default = '')
	emergency_contact_number = db.Column(db.String(255), default = '')

	### Medical History ###
	blood_type = db.Column(db.SmallInteger) 
		# 0 = O+
		# 1 = O-
		# 2 = A+
		# 3 = A-
		# 4 = B+
		# 5 = B-
		# 6 = AB+
		# 7 = AB-
	allergies = db.Column(db.Text)
	immunizations = db.Column(db.Text)
	surgeries = db.Column(db.Text)
	family_history = db.Column(db.Text)
	family_history_notes = db.Column(db.Text)
	
	## Conditions ##
	hiv = db.Column(db.Boolean)
	ht = db.Column(db.Boolean) # hypertension 
	diabetes = db.Column(db.Boolean)
	tb = db.Column(db.Boolean) # tuberculosis 
	epilepsy = db.Column(db.Boolean)
	asthma = db.Column(db.Boolean)
	sickle_cell_anemia = db.Column(db.Boolean)
	heart_condition = db.Column(db.Boolean)
	blood_transfusion = db.Column(db.Boolean)
	
	## Habits ##
	tea = db.Column(db.Boolean)
	coffee = db.Column(db.Boolean)
	drugs = db.Column(db.Boolean)
	alcohol = db.Column(db.Boolean)
	
	## Menstrual Cycle ##
	period_age_start = db.Column(db.SmallInteger)
	period_last_date = db.Column(db.Date)

	## Lab_ID - relationship
	## Prescription_ID - relationship
	## Photo
	## Dental History


	# def __init__(self, name_first, name_last, nickname, birth_date, age, \
	# 	gender, phone, address, references, occupation, children_count, \
	# 	name_mother, name_caretaker, relationship_caretaker, emergency_contact_person, \
	# 	emergency_contact_number, blood_type, allergies, immunizations, surgeries, \
	# 	family_history, family_history_notes, hiv, ht, diabetes, tb, epilepsy, \
	# 	asthma, sickle_cell_anemia, heart_condition, blood_transfusion, tea, \
	# 	coffee, drugs, alcohol, period_age_start, period_last_date):
	# 	self.name_first = name_first	
	# 	self.name_last = name_last
	# 	self.nickname = nickname
	# 	self.birth_date = birth_date
	# 	self.age = age
	# 	self.gender = gender
	# 	self.phone = phone
	# 	self.address = address
	# 	self.references = references
	# 	self.occupation = occupation
	# 	self.children_count = children_count
	# 	self.name_mother = name_mother
	# 	self.name_caretaker = name_caretaker
	# 	self.relationship_caretaker = relationship_caretaker
	# 	self.emergency_contact_person = emergency_contact_person
	# 	self.emergency_contact_number = emergency_contact_number
	# 	self.blood_type = blood_type
	# 	self.allergies = allergies
	# 	self.immunizations = immunizations
	# 	self.surgeries = surgeries
	# 	self.family_history = family_history
	# 	self.family_history_notes = family_history_notes
	# 	self.hiv = hiv
	# 	self.ht = ht
	# 	self.diabetes = diabetes
	# 	self.tb = tb
	# 	self.epilepsy = epilepsy
	# 	self.asthma = asthma
	# 	self.sickle_cell_anemia = sickle_cell_anemia
	# 	self.heart_condition = heart_condition
	# 	self.blood_transfusion = blood_transfusion
	# 	self.tea = tea
	# 	self.coffee = coffee
	# 	self.drugs = drugs
	# 	self.alcohol = alcohol
	# 	self.period_age_start = period_age_start
	# 	self.period_last_date = period_last_date


 	def __repr__(self):
 		return '<Patient %r>' % self.id


# class Visit_Doc(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
	
class Visit(db.Model):
	__tablename__ = 'Visit'
	id = db.Column(db.Integer, primary_key=True)
	visit_type = db.Column(db.SmallInteger) # 0 = doctor, 1 = dentist
	ticket_number = db.Column(db.SmallInteger)
	payment_type = db.Column(db.SmallInteger) # types and values TBD
	payment_amount = db.Column(db.Float())

	### Vitals_Doctor ###
	weight_doctor = db.Column(db.Float())
	height = db.Column(db.String(255))
	temperature = db.Column(db.Float())
	bp_doc_systolic = db.Column(db.SmallInteger)
	bp_doc_diastolic = db.Column(db.SmallInteger)
	pulse = db.Column(db.SmallInteger)
	respirations = db.Column(db.Float())

	### Vitals_Dentist ###
	weight_dentist = db.Column(db.Float())
	bp_dentist_systolic = db.Column(db.SmallInteger)
	bp_dentist_diastolic = db.Column(db.SmallInteger)

	### Doctor Exam Notes ###
	chief_complaint = db.Column(db.Text)
	hpi = db.Column(db.Text)   # history of present illness
	exam = db.Column(db.Text)
	diagnosis_doctor = db.Column(db.Text)
	treatment_doctor = db.Column(db.Text)
#### EXACT METHOD STILL TO BE DETERMINED ####
	prescription_1_doctor = db.Column(db.String(255))
	prescription_2_doctor = db.Column(db.String(255))
	prescription_3_doctor = db.Column(db.String(255))
	prescription_4_doctor = db.Column(db.String(255))
	prescription_1_notes_doctor = db.Column(db.Text)
	prescription_2_notes_doctor = db.Column(db.Text)
	prescription_3_notes_doctor = db.Column(db.Text)
	prescription_4_notes_doctor = db.Column(db.Text)
	lab_test_1_doctor = db.Column(db.String(255))
	lab_test_2_doctor = db.Column(db.String(255))
	lab_test_3_doctor = db.Column(db.String(255))
	lab_test_4_doctor = db.Column(db.String(255))
	lab_test_1_notes_doctor = db.Column(db.Text)
	lab_test_2_notes_doctor = db.Column(db.Text)
	lab_test_3_notes_doctor = db.Column(db.Text)
	lab_test_4_notes_doctor = db.Column(db.Text)

	### Dentist Exam Notes ###
	## Reason for Consultation ##
	sharp_pain = db.Column(db.Boolean)
	bleeding = db.Column(db.Boolean)
	dental_sensitivity = db.Column(db.Boolean)
	tooth_mobility = db.Column(db.Boolean)
	abscess = db.Column(db.Boolean)
	other_reason = db.Column(db.Boolean)
	other_reason_text = db.Column(db.Text)
	## Exam ##
	tooth_numbers_treated = db.Column(db.String(400))
	diagnosis_dentist = db.Column(db.Text)
	treatment_dentist = db.Column(db.Text)
	prescription_1_dentist = db.Column(db.String(255))
	prescription_1_notes_dentist = db.Column(db.Text)
	prescription_2_dentist = db.Column(db.String(255))
	prescription_2_notes_dentist = db.Column(db.Text)
	prescription_3_dentist = db.Column(db.String(255))
	prescription_3_notes_dentist = db.Column(db.Text)
	prescription_4_dentist = db.Column(db.String(255))
	prescription_4_notes_dentist = db.Column(db.Text)
	lab_test_1_dentist = db.Column(db.String(255))
	lab_test_1_notes_dentist = db.Column(db.Text)
	lab_test_2_dentist = db.Column(db.String(255))
	lab_test_2_notes_dentist = db.Column(db.Text)
	lab_test_3_dentist = db.Column(db.String(255))
	lab_test_3_notes_dentist = db.Column(db.Text)
	lab_test_4_dentist = db.Column(db.String(255))
	lab_test_4_notes_dentist = db.Column(db.Text)
	# Patient_ID - relationship

	# def __init__(self, visit_type, ticket_number, payment_type, payment_amount, weight_doctor, \
	# 	height, temperature, bp_doc_systolic, bp_doc_diastolic, pulse, respirations, weight_dentist, \
	# 	bp_dentist_systolic, bp_dentist_diastolic, chief_complaint, hpi, exam, diagnosis_doctor, \
	# 	treatment_doctor, prescription_1_doctor, prescription_2_doctor, prescription_3_doctor, \
	# 	prescription_4_doctor, prescription_1_notes_doctor, prescription_2_notes_doctor, \
	# 	prescription_3_notes_doctor, prescription_4_notes_doctor, prescription_1_dentist, \
	# 	prescription_2_dentist, prescription_3_dentist, prescription_4_dentist, \
	# 	prescription_1_notes_dentist, prescription_2_notes_dentist, prescription_3_notes_dentist, \
	# 	prescription_4_notes_dentist, lab_test_1_doctor, lab_test_2_doctor, lab_test_3_doctor, \
	# 	lab_test_4_doctor, lab_test_1_dentist, lab_test_2_dentist, lab_test_3_dentist, \
	# 	lab_test_4_dentist, lab_test_1_notes_doctor, lab_test_2_notes_doctor, lab_test_3_notes_doctor, \
	# 	lab_test_4_notes_doctor, lab_test_1_notes_dentist, lab_test_2_notes_dentist, \
	# 	lab_test_3_notes_dentist, lab_test_4_notes_dentist, sharp_pain, bleeding, \
	# 	dental_sensitivity, tooth_mobility, abscess, other_reason, other_reason_text, \
	# 	tooth_numbers_treated, diagnosis_dentist, treatment_dentist):
	# 	self.visit_type = visit_type
	# 	self.ticket_number = ticket_number
	# 	self.payment_type = payment_type
	# 	self.payment_amount = payment_amount
	# 	self.weight_doctor = weight_doctor
	# 	self.height = height
	# 	self.temperature = temperature
	# 	self.bp_doc_systolic = bp_doc_systolic
	# 	self.bp_doc_diastolic = bp_doc_diastolic
	# 	self.pulse = pulse
	# 	self.respirations = respirations
	# 	self.weight_dentist = weight_dentist
	# 	self.bp_dentist_systolic = bp_dentist_systolic
	# 	self.bp_dentist_diastolic = bp_dentist_diastolic
	# 	self.chief_complaint = chief_complaint
	# 	self.hpi = hpi
	# 	self.exam = exam
	# 	self.diagnosis_doctor = diagnosis_doctor
	# 	self.treatment_doctor = treatment_doctor
	# 	self.prescription_1_doctor = prescription_1_doctor
	# 	self.prescription_2_doctor = prescription_2_doctor
	# 	self.prescription_3_doctor = prescription_3_doctor
	# 	self.prescription_4_doctor = prescription_4_doctor
	# 	self.prescription_1_notes_doctor = prescription_1_notes_doctor
	# 	self.prescription_2_notes_doctor = prescription_2_notes_doctor
	# 	self.prescription_3_notes_doctor = prescription_3_notes_doctor
	# 	self.prescription_4_notes_doctor = prescription_4_notes_doctor
	# 	self.prescription_1_dentist = prescription_1_dentist
	# 	self.prescription_2_dentist = prescription_2_dentist
	# 	self.prescription_3_dentist = prescription_3_dentist
	# 	self.prescription_4_dentist = prescription_4_dentist
	# 	self.prescription_1_notes_dentist = prescription_1_notes_dentist
	# 	self.prescription_2_notes_dentist = prescription_2_notes_dentist
	# 	self.prescription_3_notes_dentist = prescription_3_notes_dentist
	# 	self.prescription_4_notes_dentist = prescription_4_notes_dentist
	# 	self.sharp_pain = sharp_pain
	# 	self.bleeding = bleeding
	# 	self.dental_sensitivity = dental_sensitivity
	# 	self.tooth_mobility = tooth_mobility
	# 	self.abscess = abscess
	# 	self.other_reason = other_reason
	# 	self.other_reason_text = other_reason_text
	# 	self.tooth_numbers_treated = tooth_numbers_treated
	# 	self.diagnosis_dentist = diagnosis_dentist
	# 	self.treatment_dentist = treatment_dentist

 	def __repr__(self):
 		return '<Doctor Visit %r>' % self.id

#### STILL TO BE DETERMINED ####
# class Lab(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
	# Type
	# Value
	# Visit_ID - relationship

#	def __init__(self):
#			

# 	def __repr__(self):
# 		return '<Lab %r>' % self.id


class Prescription(db.Model):
	__tablename__ = 'Prescription'
	id = db.Column(db.Integer, primary_key=True)
	given_prescription = db.Column(db.String(255))
	amount_given = db.Column(db.String(255))
	notes_prescription = db.Column(db.Text)
	
	# Visit_ID - relationship

	def __init__(self, given_prescription, amount_given, notes_prescription):
		self.given_prescription = given_prescription
		self.amount_given = amount_given
		self.notes_prescription = notes_prescription

 	def __repr__(self):
 		return '<Prescription %r>' % self.id



class status_log(db.Model):
	__tablename__ = 'status_log'
	id = db.Column(db.Integer, primary_key=True)
	visit_id = db.Column(db.SmallInteger)
#### NUMBERING SYSTEM STILL TO BE DETERMINED ####
	status = db.Column(db.SmallInteger)
	timestamp = db.Column(db.DateTime)

	def __init__(self, visit_id, status, timestamp):
		self.visit_id = visit_id
		self.status = status
		self.timestamp = timestamp

 	def __repr__(self):
 		return '<status_log %r>' % self.id