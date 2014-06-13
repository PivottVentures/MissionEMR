from flask_wtf import Form
from wtforms import StringField, SubmitField, IntegerField, RadioField, PasswordField, SelectField, DateField, TextAreaField, DecimalField, FloatField, BooleanField
from wtforms.validators import Required, Length


### Login Forms ###

class Login(Form):
	username = StringField("Nom d'utilisateur / Username", validators=[Required(), Length(1, 64)])
	password = PasswordField('Mot de passe / Password', validators=[Required()])
	submit = SubmitField('Signer Dans / Sign In')


### Test Forms ###

class Patients(Form):
	first_name = StringField('Prenom/First Name', validators=[Required()])
	last_name = StringField('Nom/Last Name', validators=[Required()])
	sex = RadioField('Sex/Gender', choices=[(0,'Male/Male'), (1,'Femelle/Female')])
	age = IntegerField('Age/Age')
	submit = SubmitField('Soumettre/Submit')


### Base Forms ###

class Search(Form):
	search_by = SelectField('Recherche Par/ Search By', choices=[('first_name', 'Prenom/First Name'), ('last_name', 'Nom/Last Name')]) 
	search_term = StringField('Search Term')
	submit = SubmitField('Chercher/Search')

class Date_Range(Form):
	start_date = DateField('Date de Debut / Start Date')
	end_date = DateField('Date de Fin / End Date')

class Contact(Form):
	contact_name = StringField('Prenom / Name')
	reason = TextAreaField('Reason')


### Registration ###

class New_Patient(Form):
	last_name = StringField('Nom / Last Name', validators=[Required()])
	first_name = StringField('Prenom / First Name', validators=[Required()])
	birth_date = DateField('Date de Naissance / Date of Birth', validators=[Required()])
	age = IntegerField('Age/Age')
	gender = RadioField('Sex/Gender', choices=[(0,'Male/Male'), (1,'Femelle/Female')], validators=[Required()])
	children_count = IntegerField("Nombre d'enfants / Number of Children", validators=[Required()])
	address = StringField('Adresse / Address')
	phone = StringField('Telephone / Phone')
	occupation = StringField('Occupation / Occupation')
	mother_name = StringField("Nom de la Mere / Mother's Name")
	guardian = StringField('Tuteur / Guardian')
	relation = StringField('Parente / Relationship')

### Payment ###

class Payment(Form):
	patient_number = IntegerField('Nombre des Patiens / Patient Number')
	payment_type = RadioField('Type de Paiement / Payment Type', choices=[(0, 'Argent/Money'), (1, "Carte D'abonnement/Pass"), (2, "Autre/Other")])
	payment_other = StringField('Autres Conditions / Other Payment')
	payment_amount = DecimalField('Montant/Amount', places=2, rounding=None)


### Triage ###

class Background(Form):
	ht = RadioField('HT', choices=[(0,'Oui/Yes'), (1,'Non/No')])
	diabetes = RadioField('Diabete / Diabetes', choices=[(0,'Oui/Yes'), (1,'Non/No')])
	asthma = RadioField('Asthme / Asthma', choices=[(0,'Oui/Yes'), (1,'Non/No')])
	epilepsy = RadioField('Epilepsie / Epilepsy', choices=[(0,'Oui/Yes'), (1,'Non/No')])
	TB = RadioField('TB', choices=[(0,'Oui/Yes'), (1,'Non/No')])
	sickle_cell = RadioField('Drepanocytose / Sickle Cell', choices=[(0,'Oui/Yes'), (1,'Non/No')])
	tea = RadioField('The / Tea', choices=[(0,'Oui/Yes'), (1,'Non/No')])
	coffee = RadioField('Cafe / Coffee', choices=[(0,'Oui/Yes'), (1,'Non/No')])
	alcohol = RadioField('Alcool / Alcohol', choices=[(0,'Oui/Yes'), (1,'Non/No')])
	drugs = RadioField('La Drogues / Drugs', choices=[(0,'Oui/Yes'), (1,'Non/No')])
	drugs_notes = TextAreaField('La Drogues Notes / Drugs Notes')
	period_age_start = DateField('Regles de Premiere / First Period')
	period_last_date = DateField('Regles de Dernier/ Last Period')
	allergies = TextAreaField('Allergies / Allergies')
	immunizations = TextAreaField('Vaccinations / Immunizations')
	surgeries = TextAreaField('Chirurgies / Surgeries')
	family_history = TextAreaField('Histoire de Famille / Family History')
	patient_notes = TextAreaField('Remarques Patients / Patient Notes')


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
