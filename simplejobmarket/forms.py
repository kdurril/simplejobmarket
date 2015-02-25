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
                    RadioField, PasswordField
from wtforms.validators import DataRequired, Length, Required

#remove models?
#from internaljobmarket.models import StudentModel,\
#                                SupervisorModel, PositionModel,\
#                                ApplicationModel, OfferModel

#class ClassicExampleForm(Form):
#    example_name = TextField('Name', validators=[DataRequired()])
#    example_description = TextAreaField('Description', validators=[DataRequired()])

class UserForm(Form):
    user_id = HiddenField('User ID')
    username = TextField('User Name', validators=[Length(min=2, max=128)])
    password = PasswordField('Password', validators=[Required()])
    role_id = HiddenField('Role ID', default="3")

class StudentForm(Form):
    name_last = TextField('Last Name', validators=[Length(min=1, max=100)], default="Smith")
    name_first = TextField('First Name', validators=[Length(min=1, max=100)])
    student_uid = TextField('Student UID', validators=[Length(9)])
    email = TextField('Email Address', validators=[Length(min=6, max=35)])
    phone = TextField('Phone', validators=[Length(min=1, max=25)])
    major = TextField('Specialization', validators=[Length(min=1, max=25)])
    program_code = TextField('Program Code', validators=[Length(min=1, max=25)])
    sem_begin = TextField('Beginning Semester', validators=[Length(min=1, max=25)])
    graduation_expected  = TextField('Expected Graduation', validators=[Length(min=1, max=25)])
    credit_fall = TextField('Fall Credit', validators=[Length(min=1, max=25)])
    credit_spring = TextField('Spring Credit', validators=[Length(min=1, max=25)])
    request_fall = BooleanField('Fall Request', validators=[Required()])
    request_spring = BooleanField('Spring Request')
    
class SupervisorForm(Form):
    name_last = TextField('Last Name', validators=[Length(min=2, max=25)])
    name_first = TextField('First Name', validators=[Length(min=1, max=25)])
    supervisor_id = TextField('Supervisor UID', validators=[Length(min=1, max=25)])
    email = TextField('Email Address', validators=[Length(min=6, max=35)])
    room = TextField('Room')
    center = TextField('Center')
    
class PositionForm(Form):
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
    available = IntegerField('Available Positions', validators=[Required()])
    supervisor_id = TextField('Supervisor ID', validators=[Required()])

class ApplicationForm(Form):
    app_id = HiddenField()
    student_uid = TextField('Student Directory ID')
    position_id = HiddenField('Position ID')

class OfferForm(Form):
    offer_id = HiddenField()
    app_id = HiddenField()
    offer_made = RadioField('Offer', choices=[('Yes', 'Yes'), ('No', 'No')])
    offer_date = DateField('Open Date')
    response = RadioField('Response', choices=[('Yes', 'Yes'), ('No', 'No')])
    response_date = HiddenField()
    available = DateField('Date Available')