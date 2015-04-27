from . import db  # . login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(64))
    role = db.Column(db.SmallInteger, default=3)  # 0 = admin, 1 = manager, 2 = doctor, 3 = nurse
#   pwhash = db.Column(db.String(128))
#   visit = db.relationship('Visit', backref='User', lazy='dynamic')

    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role
#        self.pwhash = generate_password_hash(password)

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
    __tablename__ = 'Patient'
    id = db.Column(db.Integer, primary_key=True)

    ## Demographics ##
    name_first = db.Column(db.String(255), default='')
    name_last = db.Column(db.String(255), default='')
    nickname = db.Column(db.String(255), default='')
    birth_date = db.Column(db.Date)  # attributes: year, month, day
    age = db.Column(db.SmallInteger)
    gender = db.Column(db.String(6))
    phone = db.Column(db.String(255), default='')
    address = db.Column(db.String(255), default='')
    references = db.Column(db.String(255), default='')
    occupation = db.Column(db.String(255), default='')
    children_count = db.Column(db.SmallInteger, default=0)
    name_mother = db.Column(db.String(255), default='')
    name_caretaker = db.Column(db.String(255), default='')
    relationship_caretaker = db.Column(db.String(255), default='')
    emergency_contact_person = db.Column(db.String(255), default='')
    emergency_contact_number = db.Column(db.String(255), default='')

    ### Blood Type ###
    blood_type = db.Column(db.String(6)) # Select, O+, O-, A+, A-, B+, B-, AB+, AB-
    
    ## Conditions ##
    ht = db.Column(db.Boolean, default=False)  # hypertension
    tb = db.Column(db.Boolean, default=False)  # tuberculosis
    asthma = db.Column(db.Boolean, default=False)
    heart_condition = db.Column(db.Boolean, default=False)
    hiv = db.Column(db.Boolean, default=False)
    diabetes = db.Column(db.Boolean, default=False)
    epilepsy = db.Column(db.Boolean, default=False)
    sickle_cell_anemia = db.Column(db.Boolean, default=False)
    blood_transfusion = db.Column(db.Boolean, default=False)

    ## Habits ##
    tea = db.Column(db.Boolean, default=False)
    coffee = db.Column(db.Boolean, default=False)
    drugs = db.Column(db.Boolean, default=False)
    alcohol = db.Column(db.Boolean, default=False)

    ## Menstrual Cycle ##
    period_age_start = db.Column(db.SmallInteger)

    ### Medical History ###
    allergies = db.Column(db.Text, default='')
    immunizations = db.Column(db.Text, default='')
    surgeries = db.Column(db.Text, default='')
    family_history = db.Column(db.Text, default='')
    family_history_notes = db.Column(db.Text, default='')
    ## Photo
    ## Dental History
    ## Past dental vists

    ### Relationships ###
    lab_patient = db.relationship('Lab', backref='patient')
    visit_patient = db.relationship('Visit', backref='patient')
    prescription_patient = db.relationship('Prescription', backref='patient')

#     def __init__(self, name_first, name_last, nickname, birth_date, age,
#         gender, phone, address, references, occupation, children_count,
#         name_mother, name_caretaker, relationship_caretaker, emergency_contact_person,
#         emergency_contact_number, blood_type, allergies, immunizations, surgeries,
#         family_history, family_history_notes, hiv, ht, diabetes, tb, epilepsy,
#         asthma, sickle_cell_anemia, heart_condition, blood_transfusion, tea,
#         coffee, drugs, alcohol, period_age_start, period_last_date, lab_patient, visit_patient, prescription_patient):
#         self.name_first = name_first
#         self.name_last = name_last
#         self.nickname = nickname
#         self.birth_date = birth_date
#         self.age = age
#         self.gender = gender
#         self.phone = phone
#         self.address = address
#         self.references = references
#         self.occupation = occupation
#         self.children_count = children_count
#         self.name_mother = name_mother
#         self.name_caretaker = name_caretaker
#         self.relationship_caretaker = relationship_caretaker
#         self.emergency_contact_person = emergency_contact_person
#         self.emergency_contact_number = emergency_contact_number
#         self.blood_type = blood_type
#         self.allergies = allergies
#         self.immunizations = immunizations
#         self.surgeries = surgeries
#         self.family_history = family_history
#         self.family_history_notes = family_history_notes
#         self.hiv = hiv
#         self.ht = ht
#         self.diabetes = diabetes
#         self.tb = tb
#         self.epilepsy = epilepsy
#         self.asthma = asthma
#         self.sickle_cell_anemia = sickle_cell_anemia
#         self.heart_condition = heart_condition
#         self.blood_transfusion = blood_transfusion
#         self.tea = tea
#         self.coffee = coffee
#         self.drugs = drugs
#         self.alcohol = alcohol
#         self.period_age_start = period_age_start
#         self.period_last_date = period_last_date
#         self.lab_patient = lab_patient
#         self.visit_patient = visit_patient
#         self.prescription_patient = prescription_patient

    def __repr__(self):
        return '<Patient %r>' % self.id



class Visit(db.Model):
    __tablename__ = 'Visit'
    id = db.Column(db.Integer, primary_key=True)
    visit_date = db.Column(db.Date)
    
    ### Registration Payment ###
    visit_type = db.Column(db.SmallInteger)  # 0 = doctor, 1 = dentist
    ticket_number = db.Column(db.SmallInteger)
    payment_type = db.Column(db.String(15))  # types and values TBD
    payment_other_amount = db.Column(db.Float(), default=0)
    payment_notes = db.Column(db.Text, default='')

    ### Vitals_Doctor ###
    weight = db.Column(db.Float())
    height = db.Column(db.String(255))
    temperature = db.Column(db.Float())
    bp_systolic = db.Column(db.SmallInteger)
    bp_diastolic = db.Column(db.SmallInteger)
    pulse = db.Column(db.SmallInteger)
    respirations = db.Column(db.Float())
    period_last_date = db.Column(db.Date)

    ### Doctor Exam Notes ###
    chief_complaint = db.Column(db.Text)
    hpi = db.Column(db.Text)   # history of present illness
    exam = db.Column(db.Text)
    diagnosis_doctor = db.Column(db.Text)
    treatment_doctor = db.Column(db.Text)

    ### Dentist Exam Notes ###

    ## Reason for Consultation ##
    sharp_pain = db.Column(db.Boolean)
    dental_sensitivity = db.Column(db.Boolean)
    bleeding = db.Column(db.Boolean)
    abscess = db.Column(db.Boolean)
    tooth_mobility = db.Column(db.Boolean)
    other_reason = db.Column(db.Boolean)
    other_reason_text = db.Column(db.Text)
    ## Exam ##
    tooth_numbers_treated = db.Column(db.String(400))
    diagnosis_dentist = db.Column(db.Text)
    treatment_dentist = db.Column(db.Text)

    ### Relationships ###
#    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    visit_patient_id = db.Column(db.Integer, db.ForeignKey('Patient.id'))
    lab_visit = db.relationship('Lab', backref='visit')
    prescription_visit = db.relationship('Prescription', backref='visit')
    statusLog_visit = db.relationship('StatusLog', backref='visit')

#     def __init__(self, visit_type, ticket_number, payment_type, payment_amount, weight_doctor, \
#         height, temperature, bp_doc_systolic, bp_doc_diastolic, pulse, respirations, weight_dentist, \
#         bp_dentist_systolic, bp_dentist_diastolic, chief_complaint, hpi, exam, diagnosis_doctor, \
#         treatment_doctor, sharp_pain, bleeding, dental_sensitivity, tooth_mobility, abscess, \
#         other_reason, other_reason_text, tooth_numbers_treated, diagnosis_dentist, treatment_dentist, \
#         user_id, patient_id, lab_visit, prescription_visit, Status_Log_visit):
#         self.visit_type = visit_type
#         self.ticket_number = ticket_number
#         self.payment_type = payment_type
#         self.payment_amount = payment_amount
#         self.weight_doctor = weight_doctor
#         self.height = height
#         self.temperature = temperature
#         self.bp_doc_systolic = bp_doc_systolic
#         self.bp_doc_diastolic = bp_doc_diastolic
#         self.pulse = pulse
#         self.respirations = respirations
#         self.weight_dentist = weight_dentist
#         self.bp_dentist_systolic = bp_dentist_systolic
#         self.bp_dentist_diastolic = bp_dentist_diastolic
#         self.chief_complaint = chief_complaint
#         self.hpi = hpi
#         self.exam = exam
#         self.diagnosis_doctor = diagnosis_doctor
#         self.treatment_doctor = treatment_doctor
#         self.sharp_pain = sharp_pain
#         self.bleeding = bleeding
#         self.dental_sensitivity = dental_sensitivity
#         self.tooth_mobility = tooth_mobility
#         self.abscess = abscess
#         self.other_reason = other_reason
#         self.other_reason_text = other_reason_text
#         self.tooth_numbers_treated = tooth_numbers_treated
#         self.diagnosis_dentist = diagnosis_dentist
#         self.treatment_dentist = treatment_dentist
#         self.user_id = user_id
#         self.patient_id = patient_id
#         self.lab_visit = lab_visit
#         self.prescription_visit = prescription_visit
#         self.Status_Log_visit = Status_Log_visit

    def __repr__(self):
        return '<Visit %r>' % self.id



class StatusLog(db.Model):
    __tablename__ = 'StatusLog'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.SmallInteger)
    timestamp = db.Column(db.DateTime)
    statusLog_visit_id = db.Column(db.Integer, db.ForeignKey('Visit.id'))

    def __init__(self, status, timestamp, statusLog_visit_id):
        self.status = status
        self.timestamp = timestamp
        self.visit_id = statusLog_visit_id

    def __repr__(self):
        return '<StatusLog %r>' % self.id



class Lab(db.Model):
    __tablename__ = 'Lab'
    id = db.Column(db.Integer, primary_key=True)
    prescribed_test = db.Column(db.Text)
    test_notes = db.Column(db.Text)
    # Type
    # Value

    ### Relationships ###
    lab_patient_id = db.Column(db.Integer, db.ForeignKey('Patient.id'))
    lab_visit_id = db.Column(db.Integer, db.ForeignKey('Visit.id'))

#     def __init__(self, prescribed_test, test_notes, patient_id, visit_id):
#         self.prescribed_test = prescribed_test
#         self.test_notes = test_notes
#         self.patient_id = patient_id
#         self.visit_id = visit_id

    def __repr__(self):
        return '<Lab %r>' % self.id



class Prescription(db.Model):
    __tablename__ = 'Prescription'
    id = db.Column(db.Integer, primary_key=True)
    doctor_prescription = db.Column(db.Text)
    dentist_prescription = db.Column(db.Text)
    given_prescription = db.Column(db.String(255))
    amount_given = db.Column(db.String(255))
    notes_pharmacy = db.Column(db.Text)

    ### Relationships ###
    prescription_patient_id = db.Column(db.Integer, db.ForeignKey('Patient.id'))
    prescription_visit_id = db.Column(db.Integer, db.ForeignKey('Visit.id'))

#     def __init__(self, doctor_prescription, dentist_prescription, given_prescription, \
#         amount_given, notes_pharmacy, patient_id, visit_id):
#         self.doctor_prescription = doctor_prescription
#         self.dentist_prescription = dentist_prescription
#         self.given_prescription = given_prescription
#         self.amount_given = amount_given
#         self.notes_pharmacy = notes_pharmacy
#         self.patient_id = patient_id
#         self.visit_id = visit_id

    def __repr__(self):
        return '<Prescription %r>' % self.id
