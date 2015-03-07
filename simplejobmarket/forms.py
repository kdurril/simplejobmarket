#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
forms.py

Web forms based on Flask-WTForms

See: http://flask.pocoo.org/docs/patterns/wtforms/
http://wtforms.simplecodes.com/

"""
#import wtf
#from wtf import wtf, validators
#from flaskext import wtf
#from flaskext.wtf import validators

from flask_wtf import Form
from wtforms import StringField, TextField, TextAreaField, BooleanField,\
                    SelectField, DateField, IntegerField, HiddenField,\
                    RadioField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Required, Email

class UserForm(Form):
    username = TextField('Directory ID', validators=[Length(min=2, max=128)])
    password = PasswordField('Password', validators=[Required()])
    role_id = HiddenField('Role ID', default="1")
    #id = HiddenField('ID')
    remember = BooleanField('Stay logged in')
    submit = SubmitField('Submit')

class RegistrationForm(UserForm):
    role_id = IntegerField('Role', default=1)
    #role_id = SelectField('Role ID',\
    #                      choices=[(1, 1),\
    #                               (2, 2)])

class StudentForm(Form):
    username = HiddenField('Username')
    name_last = TextField('Last Name', validators=[Length(min=1, max=100)], default="Smith")
    name_first = TextField('First Name', validators=[Length(min=1, max=100)])
    student_uid = TextField('Student UID', validators=[Length(9)])
    email = TextField('Email Address', validators=[Required(), Email()])
    phone = TextField('Phone', validators=[Length(min=1, max=25)])
    major = TextField('Specialization', validators=[Length(min=1, max=25)])
    program_code = TextField('Program Code', validators=[Length(min=1, max=25)])
    sem_begin = TextField('Beginning Semester', validators=[Length(min=1, max=25)])
    graduation_expected  = TextField('Expected Graduation', validators=[Length(min=1, max=25)])
    credit_fall = TextField('Fall Credit', validators=[Length(min=1, max=25)])
    credit_spring = TextField('Spring Credit', validators=[Length(min=1, max=25)])
    request_fall = BooleanField('Fall Request', validators=[Required()])
    request_spring = BooleanField('Spring Request')
    submit = SubmitField('Submit')
    
class SupervisorForm(Form):
    username = HiddenField('Username')
    name_last = TextField('Last Name', validators=[Length(min=2, max=25)])
    name_first = TextField('First Name', validators=[Length(min=1, max=25)])
    supervisor_id = TextField('Supervisor UID', validators=[Length(min=1, max=25)])
    email = TextField('Email Address', validators=[Required(), Email()])
    room = TextField('Room')
    center = TextField('Center')
    submit = SubmitField('Submit')
    
class PositionForm(Form):
    
    username = HiddenField('Username')
    title = TextField('Title', validators=[Length(min=2, max=255)])
    work_group = TextField('Center or Work Group')
    position_type = SelectField('Position Type',\
                                choices=[('GA', 'Graduate Assistant'),\
                                        ('AA', 'Administrative Assistant'),\
                                        ('RA', 'Research Assistant'),\
                                        ('TA', 'Teaching Assistant')])
    course = SelectField('Course',\
                            choices=[('PUAF610', 'PUAF610'),\
                                    ('PUAF611', 'PUAF611'),\
                                    ('PUAF620', 'PUAF620'),\
                                    ('PUAF640', 'PUAF640'),\
                                    ('PUAF641', 'PUAF641'),\
                                    ('PUAF670', 'PUAF670'),\
                                    ('PUAF781', 'PUAF781')])
    program_min = SelectField('Min Program Level',\
                            choices=[('M1', 'Masters 1st Year'),\
                                    ('M2', 'Masters 2nd Year'),\
                                    ('Phd1', 'PhD 1st Year'),\
                                    ('Phd2', 'PhD 2nd Year'),\
                                    ('PhdCadidate', 'PhD Candidate')])
    program_std = SelectField('Standard Program Level',\
                            choices=[('M1', 'Masters 1st Year'),\
                                    ('M2', 'Masters 2nd Year'),\
                                    ('Phd1', 'PhD 1st Year'),\
                                    ('Phd2', 'PhD 2nd Year'),\
                                    ('PhdCadidate', 'PhD Candidate')])
    position_overview = TextAreaField('Position Overview', validators=[Length(min=2, max=255)])
    primary_duties = TextAreaField('Primary Duties', validators=[Length(min=2, max=255)])
    necessary_skill = TextAreaField('Required Skills', validators=[Length(min=2, max=255)])
    preferred_skill = TextAreaField('Additional Skills', validators=[Length(min=2, max=255)])
    date_open = DateField('Open Date')
    date_closed = DateField('Close Date')
    available = IntegerField('Available', default=1)
    submit = SubmitField('Submit')

class ApplicationForm(Form):
    username = HiddenField('Username')
    position_id = HiddenField()
    submit = SubmitField('Apply')

class OfferForm(Form):
    'Accept or reject applicant by supervisor'
    #offer_id = HiddenField()
    app_id = HiddenField()
    offer_made = RadioField('Offer', choices=[('Yes', 'Yes'), ('No', 'No')])
    #offer_date = DateField('Open Date') LET THIS BE A AUTO STAMP
    submit = SubmitField('Conclude')

class ResponseForm(Form):
    'This is the version for accepting or rejecting the offer by student'
    response = RadioField('Response', choices=[('Yes', 'Yes'), ('No', 'No')])
    response_date = HiddenField()
    available = DateField('Date Available')
    submit = SubmitField('Respond')