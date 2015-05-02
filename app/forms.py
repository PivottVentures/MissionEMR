from flask_wtf import Form
from wtforms import StringField, SubmitField, IntegerField, RadioField, PasswordField, SelectField, \
					DateField, TextAreaField, DecimalField, FloatField, BooleanField
from wtforms.validators import Required, Length, InputRequired, Optional,\
	optional


### Login Forms ###

class Login(Form):
	username = StringField("Username", validators=[Required(), Length(1, 64)])
	password = PasswordField('Password', validators=[Required()])

### Test Forms ###

class Patients(Form):
	name_first = StringField('First Name', validators=[Required()])
	name_last = StringField('Last Name', validators=[Required()])
	age = IntegerField('Age', validators=[Required()])
	gender = RadioField('Gender', choices=[(0,'Male'), (1,'Female')], coerce=int)


class Registration_Search(Form):
	criteria = SelectField('Search By', choices=[('name_last', 'Last Name'), \
						('name_first', 'First Name'), ('phone', 'Phone'), \
						('address', 'Address'), ('id', 'Patient Number')])
	search_term = StringField('Search Term', validators=[Required()])






### Registration ###

class Registration_Patient(Form): # DONE!
	name_first = StringField('First Name', validators=[Required()])
	name_last = StringField('Last Name', validators=[Required()])
	nickname = StringField('Nickname')
	birth_date = DateField('Date of Birth', format='%m/%d/%Y', validators=[Required()])
	age = IntegerField('Age', validators=[Required()])
	gender = RadioField('Gender', choices=[('Male','Male'), ('Female','Female')], validators=[Required()])
	phone = StringField('Phone', validators=[Required()])
	address = StringField('Address', validators=[Required()])
	children_count = IntegerField("Number of Children", validators=[InputRequired()])
	references = StringField('References')
	occupation = StringField('Occupation')
	mother_name = StringField("Mother's Name")
	caretaker = StringField('Caretaker')
	caretaker_relation = StringField('Relationship')
	emergency_person = StringField('Emergency Contact Person')
	emergency_number = StringField('Emergency Contact Number')

class Payment(Form):  
	ticket_number = IntegerField('Ticket Number', validators=[Required()])
	payment_type = RadioField('Payment Type', choices=[('Money', 'Money'), ('Pink', "Pink Pass"), 
																			('Blue', "Blue Pass"), ('Yellow', "Yellow Pass"),
																			('Other', "Other")], validators=[Required()])
	payment_amount = DecimalField('Other Amount', places=2, rounding=None, validators=[optional()])
	payment_notes = StringField('Notes')


### Vitals ###

class Background(Form):
	# Blood Type
	blood_type = SelectField('Blood Type', choices=[('Select', 'Select'), 
												('O+', 'O+'), ('O+', 'O-'), 
												('A+', 'A+'), ('A-', 'A-'), 
												('B+', 'B+'), ('B-', 'B-'), 
												('AB+', 'AB+'), ('AB-', 'AB-')])

	# Conditions
	hiv = BooleanField('HIV')
	ht = BooleanField('Hypertension')
	diabetes = BooleanField('Diabetes')
	tb = BooleanField('Tuberculosis')
	epilepsy = BooleanField('Epilepsy')
	asthma = BooleanField('Asthma')
	sickle_cell_anemia = BooleanField('Sickle Cell')
	heart_condition = BooleanField('Heart Condition')
	blood_transfusion = BooleanField('Blood Transfusion')

	# Habits
	tea = BooleanField('Tea')
	coffee = BooleanField('Coffee')
	drugs = BooleanField('Drugs')
	alcohol = BooleanField('Alcohol')

	# Menstrual Cycle
	period_age_start = IntegerField('First Period', validators=[Optional()])

	# Medical History
	allergies = TextAreaField('Allergies')
	immunizations = TextAreaField('Immunizations')
	surgeries = TextAreaField('Surgeries')
	family_history = TextAreaField('Family History')
	background_notes = TextAreaField('Background Notes')

class Vitals_Vitals(Form):
	weight = FloatField('Weight')
	height = FloatField('Height')
	bp_systolic = IntegerField('Systolic')
	bp_diastolic = IntegerField('Diastolic')
	pulse = IntegerField('Pulse')
	temperature = FloatField('Temperature', validators=[optional()])
	respirations = FloatField('Respirations', validators=[optional()])
	period_last_date = DateField('Last Period', format='%m/%d/%Y', validators=[Optional()])
	complaint = TextAreaField('Complaint')


### Doctor Visit ###

class Doctor_Exam(Form):
	visit_date = SelectField('Visit Date:', choices=[('Today', 'Today')], coerce=unicode)
	complaint = TextAreaField('Complaint')
	history = TextAreaField('History')
	exam = TextAreaField('Exam')
	diagnosis = TextAreaField('Diagnosis')
	treatment = TextAreaField('Treatment')
	prescrip_given = BooleanField('Prescription Given')
	prescrip_descrip = TextAreaField('Prescription Description')
	lab_given = BooleanField('Lab Given')
	lab_test = TextAreaField('Lab Tests')


### Dentist ###

class Dentist_Vitals(Form):
	weight = FloatField('Weight')
	bp_systolic = IntegerField('Systolic')
	bp_diastolic = IntegerField('Diastolic')
	pain = BooleanField('Sharp Pain')
	bleeding = BooleanField('Bleeding')
	sensitivity = BooleanField('Dental Sensitivity')
	mobility = BooleanField('Tooth Mobility')
	abscess = BooleanField('Abscess')
	other = BooleanField('Other:')
	other_reason = StringField('Other:')

class Dentist_Exam(Form):
	visit_date = SelectField('Visit Date:', choices=[('Today', 'Today')], coerce=unicode)
	teeth_treated = StringField("Tooth #'s Treated:" )
	diagnosis = TextAreaField('Diagnosis')
	treatment = TextAreaField('Treatment')
	prescrip_given = BooleanField('Prescription Given')
	prescrip_descrip = TextAreaField('Prescription Description')
	lab_given = BooleanField('Lab Given')
	lab_test = TextAreaField('Lab Tests')
	

### Pharmacy ###

class Pharmacy(Form):
	medication_given = StringField('Medication Given')
	amount_given = StringField('Amount Given')
	pharmacy_notes = TextAreaField('Notes')


### Base Forms ###

class Date_Range(Form):
	start_date = DateField('Start Date')
	end_date = DateField('End Date')

class Contact(Form):
	contact_name = StringField('Name')
	reason = TextAreaField('Reason')

