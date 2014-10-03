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


 class Patient(db.Model):
 	id = db.Column(db.Integer, primary_key=True)
	
	## Demographics ##
	name_first = db.Column(db.String(255))
	name_last = db.Column(db.String(255))
	nickname = db.Column(db.String(255))
	birth_date = db.Column(db.Date) # attributes: year, month, day
	age = db.Column(db.SmallInteger)
	gender = db.Column(db.SmallInteger) # 0 = male, 1 = female
	phone = db.Column(db.String(255))
	address = db.Column(db.String(255))
	references = db.Column(db.String(255))
	occupation = db.Column(db.String(255))
	children_count = db.Column(db.SmallInteger, default=0)
	name_mother = db.Column(db.String(255))
	name_caretaker = db.Column(db.String(255))
	relationship_caretaker = db.Column(db.String(255))
	emergency_contact_person = db.Column(db.String(255))
	emergency_contact_number = db.Column(db.String(255))

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
	notes = db.Column(db.Text)
	
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
	age_start = db.Column(SmallInteger)
	last_date = db.Column(Date)

	## Lab_ID - relationship
	## Prescription_ID - relationship
	## Photo
	## Dental History

	def __init__(self, name_first):
		self.name_first = name_first			

# 	def __repr__(self):
# 		return '<Patient %r>' % self.id


# class Visit_Doc(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
	
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
	exam = 
	# diagnosis_doctor
	# treatment_doctor
	# prescriptions_doctor
	# lab_tests_doctor

	### Dentist Exam Notes ###
	## Reason for Consultation ##
	# sharp_pain - checkbox
	# bleeding - checkbox
	# dental_sensitivity - checkbox
	# tooth_mobility - checkbox
	# abscess - checkbox
	# other - checkbox + field
	## Exam ##
	# tooth_number_treated
	# diagnosis_dentist
	# treatment_dentist
	# prescriptions_dentist
	# lab_tests_dentist

	# Patient_ID - relationship

#	def __init__(self):
#			

# 	def __repr__(self):
# 		return '<Doctor Visit %r>' % self.id


# class Lab(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
	# Type
	# Value
	# Visit_ID - relationship

#	def __init__(self):
#			

# 	def __repr__(self):
# 		return '<Lab %r>' % self.id


# class Prescription(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
	# given_prescription
	# amount_given
	# notes_prescription
	

	# Visit_ID - relationship

#	def __init__(self):
#			

# 	def __repr__(self):
# 		return '<Prescription %r>' % self.id


# class status_log(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
	# visit_id = 
	# status = 
	# timestamp = 

#	def __init__(self):
#			

# 	def __repr__(self):
# 		return '<status_log %r>' % self.id