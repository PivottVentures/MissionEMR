from flask_wtf import Form
from wtforms import StringField, SubmitField, IntegerField, RadioField, PasswordField, SelectField, \
					DateField, TextAreaField, DecimalField, FloatField, BooleanField
from wtforms.validators import Required, Length, InputRequired, Optional


### Login Forms ###

class Login(Form):
	username = StringField("Nom d'utilisateur / Username", validators=[Required(), Length(1, 64)])
	password = PasswordField('Mot de passe / Password', validators=[Required()])

### Test Forms ###

class Patients(Form):
	first_name = StringField('Prenom/First Name', validators=[Required()])
	last_name = StringField('Nom/Last Name', validators=[Required()])
	age = IntegerField('Age/Age', validators=[Required()])
	gender = RadioField('Sex/Gender', choices=[(0,'Male/Male'), (1,'Femelle/Female')], coerce=int)


class Registration_Search(Form):
	criteria = SelectField('Recherche Par/ Search By', choices=[('last_name', 'Nom/Last Name'), \
						('first_name', 'Prenom/First Name'), ('phone', 'Telephone/Phone'), \
						('address', 'Adresse/Address'), ('id', 'Nombre des Patiens/Patient Number')])
	search_term = StringField('Search Term', validators=[Required()])






### Registration ###

class Registration_Patient(Form): # DONE!
	first_name = StringField('Prenom / First Name', validators=[Required()])
	last_name = StringField('Nom / Last Name', validators=[Required()])
	nickname = StringField('Nom / Nickname')
	birth_date = DateField('Date de Naissance / Date of Birth', format='%m/%d/%Y', validators=[Required()])
	age = IntegerField('Age/Age', validators=[Required()])
	gender = RadioField('Sex/Gender', choices=[(0,'Male/Male'), (1,'Femelle/Female')], coerce=int)
	phone = StringField('Telephone / Phone', validators=[Required()])
	address = StringField('Adresse / Address', validators=[Required()])
	children_count = IntegerField("Nombre d'enfants / Number of Children", validators=[InputRequired()])
	references = StringField('XXXXX / References')
	occupation = StringField('Occupation / Occupation')
	mother_name = StringField("Nom de la Mere / Mother's Name")
	caretaker = StringField('Tuteur / Caretaker')
	caretaker_relation = StringField('Parente / Relationship')
	emergency_person = StringField('XXXXX / Emergency Contact Person')
	emergency_number = StringField('XXXXX / Emergency Contact Number')

class Payment(Form):  
	ticket_number = IntegerField('XXXXX / Ticket Number', validators=[Required()])
	payment_type = RadioField('Type de Paiement / Payment Type', choices=[('Money', 'Argent/Money'), ('Pink Pass', "Carte D'abonnement/Pass"), 
																			('Blue Pass', "Carte D'abonnement/Pass"), ('Yellow Pass', "Carte D'abonnement/Pass"),
																			('Other', "Autre/Other")], validators=[Required()])
	payment_amount = DecimalField('Autres Montant/Other Amount', places=2, rounding=None)
	payment_notes = StringField('XXXXX / Notes')


### Vitals ###

class Background(Form):
	# Blood Type
	blood_type = SelectField('Blood Type', choices=[(0, 'Select'), (1, 'O+'), (2, 'O-'), (3, 'A+'), (4, 'A-'), (5, 'B+'), (6, 'B-'), (7, 'AB+'), (8, 'AB-')], coerce=int)

	# Conditions
	hiv = BooleanField('HIV')
	ht = BooleanField('Hypertension')
	diabetes = BooleanField('Diabete / Diabetes')
	tb = BooleanField('Tuberculosis')
	epilepsy = BooleanField('Epilepsie / Epilepsy')
	asthma = BooleanField('Asthme / Asthma')
	sickle_cell_anemia = BooleanField('Drepanocytose / Sickle Cell')
	heart_condition = BooleanField('Drepanocytose / Sickle Cell')
	blood_transfusion = BooleanField('Drepanocytose / Sickle Cell')

	# Habits
	tea = BooleanField('The / Tea')
	coffee = BooleanField('Cafe / Coffee')
	drugs = BooleanField('La Drogues / Drugs')
	alcohol = BooleanField('Alcool / Alcohol')

	# Menstrual Cycle
	period_age_start = DateField('Regles de Premiere / First Period', validators=[Optional()])
	period_last_date = DateField('Regles de Dernier/ Last Period', validators=[Optional()])

	# Medical History
	allergies = TextAreaField('Allergies / Allergies')
	immunizations = TextAreaField('Vaccinations / Immunizations')
	surgeries = TextAreaField('Chirurgies / Surgeries')
	family_history = TextAreaField('Histoire de Famille / Family History')
	background_notes = TextAreaField('Remarques Background / Background Notes')

class Vitals(Form):
	weight = FloatField('Poids / Weight')
	height = FloatField('Hauteur / Height')
	bp_systolic = IntegerField('Systolique / Systolic')
	bp_diastolic = IntegerField('Diastolique / Diastolic')
	pulse = IntegerField('Implusion / Pulse')
	temperature = FloatField('Temperature / Temperature')
	respirations = FloatField('Respirations / Respirations')


### Doctor Visit ###

class Exam(Form):
	complaint = TextAreaField('Plainte / Complaint')
	history = TextAreaField('Histoire / History')
	exam = TextAreaField('Exam / Exam')
	diagnois = TextAreaField('Diagnostic / Diagnosis')
	treatment_1 = StringField('Traitement / Treatment 1')
	treatment_2 = StringField('Traitement / Treatment 2')
	treatment_3 = StringField('Traitement / Treatment 3')
	treatment_4 = StringField('Traitement / Treatment 4')
	treatment_5 = StringField('Traitement / Treatment 5')
	treatment_6 = StringField('Traitement / Treatment 6')
	follow_up = TextAreaField('Suivre / Follow Up')
	exam_notes = TextAreaField("Notes d'Examen / Exam Notes")
	prescrip_given = BooleanField('Compte Tenu de la Prescription / Prescription Given')
	prescrip_descrip = TextAreaField('Description de Prescription / Prescription Description')


### Pharmacy ###

class Pharmacy(Form):
	medication_given = StringField('Medicament Donne / Medication Given')
	amount_given = StringField('Quantite Donnee / Amount Given')
	pharmacy_notes = TextAreaField('Notes / Notes')


### Base Forms ###

class Date_Range(Form):
	start_date = DateField('Date de Debut / Start Date')
	end_date = DateField('Date de Fin / End Date')

class Contact(Form):
	contact_name = StringField('Prenom / Name')
	reason = TextAreaField('Reason')

