#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Flask-SQLAlchemy ORM models 

from simplejobmarket import app
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin
from . import login_manager
from . import db
import os

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:4054756UMD@localhost/postgres'
#os.environ.get('POSTGRESKEY')


#db = SQLAlchemy(app)

class RoleModel(db.Model):
    __tablename__ = 'roles'
    __table_args__ ={"schema":"jobmarket"}

    role_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24), unique=True)
    users = db.relationship("UserModel", backref=db.backref('roles'))

    def __init__(self, role_id=None, name=None):
        self.role_id=role_id
        self.name=name

    def __repr__(self):
        return 'Role Name {0}'.format(self.name)

class UserModel(UserMixin, db.Model):
    __tablename__ = 'users'
    __table_args__ = {"schema":"jobmarket"}

    username = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer,db.ForeignKey('jobmarket.roles.role_id'))
    id = db.Column(db.Integer(), primary_key=True)
    student = db.relationship("StudentModel", backref=('users'))
    supervisor = db.relationship("SupervisorModel", backref=('users'))


    def __init__(self, username=None, password_hash=None, role_id=None):
        self.username = username
        self.password_hash = password_hash
        self.role_id = role_id
        
        
    def __repr__(self):
        return self.username

    @property
    def password(self):
        raise AttributeError('password is not readable attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

class StudentModel(db.Model):
    __tablename__ = 'students'
    __table_args__ = {"schema":"jobmarket"}
    
    username = db.Column(db.String(120),\
                          db.ForeignKey('jobmarket.users.username'))
    student_uid = db.Column(db.String(120), primary_key=True)
    name_last = db.Column(db.String(120))
    name_first  = db.Column(db.String(120))
    email  = db.Column(db.String(120))
    phone  = db.Column(db.String(120))
    major  = db.Column(db.String(120))
    program_code  = db.Column(db.String(120))
    sem_begin  = db.Column(db.String(120))
    graduation_expected  = db.Column(db.String(120))
    credit_fall  = db.Column(db.Integer)
    credit_spring =  db.Column(db.Integer)
    request_fall = db.Column(db.String(120))
    request_spring = db.Column(db.String(120))
    position_apps = db.relationship("PositionAppModel",\
        backref=db.backref('students'), lazy='dynamic')
    
    def __init__(self, username=username, student_uid=None, name_last=None,
                name_first=None, email=None,
                phone=None, major=None,
                program_code=None, sem_begin=None,
                graduation_expected=None, credit_fall=None,
                credit_spring=None, request_fall=None,
                request_spring=None):
        self.username
        self.student_uid =  student_uid
        self.name_last = name_last
        self.name_first = name_first
        self.email = email
        self.phone = phone
        self.major = major
        self.program_code = program_code
        self.sem_begin = sem_begin
        self.graduation_expected = graduation_expected
        self.credit_fall = credit_fall
        self.credit_spring = credit_spring
        self.request_fall = request_fall
        self.request_spring = request_spring
        
    def __repr__(self):
        return '<{0}>'.format(self.username)

@login_manager.user_loader
def load_user(id):
    return UserModel.query.get(id)


class SupervisorModel(db.Model):
    __tablename__ = 'supervisors'
    __table_args__ = {"schema":"jobmarket"}
    username = db.Column(db.String(120),\
                          db.ForeignKey('jobmarket.users.username'))
    supervisor_id = db.Column(db.Integer, primary_key=True)
    name_last = db.Column(db.String(120))
    name_first = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    email = db.Column(db.String(120))
    room = db.Column(db.String(120))
    center = db.Column(db.String(120))
    position = db.relationship("PositionModel", 
                            backref=db.backref('supervisors'),
                            lazy='dynamic')

    def __init__(self, username=username, supervisor_id=None, 
                name_last=None, name_first=None,
                phone=None, email=None,
                room=None, center=None):
        self.username = username
        self.supervisor_id = supervisor_id
        self.name_last = name_last
        self.name_frst = name_first
        self.phone = phone
        self.email = email
        self.room = room
        self.center = center
        
    def __repr__(self):
        return '<{0}>'.format(self.username)

class PositionModel(db.Model):
    __tablename__ = 'positions'
    __table_args__ = {"schema":"jobmarket"}
    position_id  = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    work_group = db.Column(db.String(120))
    position_type = db.Column(db.String(120))
    course = db.Column(db.String(120))
    program_min = db.Column(db.String(120))
    program_std = db.Column(db.String(120))
    position_overview = db.Column(db.String(120))
    primary_duties = db.Column(db.String(120))
    necessary_skill = db.Column(db.String(120))
    preferred_skill = db.Column(db.String(120))
    date_open = db.Column(db.String(120))
    date_closed = db.Column(db.String(120))
    available = db.Column(db.Integer)
    username = db.Column(db.String(120), 
        db.ForeignKey('jobmarket.supervisors.username'), nullable=False)
    position_apps = db.relationship("PositionAppModel", 
        backref=db.backref('positions'))
    
    def __init__(self, position_id=None,
                title=None, work_group=None, position_type=None,
                course=None, program_min=None, program_std=None,
                position_overview=None, primary_duties=None,
                necessary_skill=None, preferred_skill=None,
                date_open=None, date_closed=None,
                available=None, username=username):
        self.position_id = position_id
        self.title = title
        self.work_group = work_group
        self.position_type = position_type
        self.course = course
        self.program_min = program_min
        self.program_std = program_std
        self.position_overview = position_overview
        self.primary_duties = primary_duties
        self.necessary_skill = necessary_skill
        self.preferred_skill = preferred_skill
        self.date_open = date_open
        self.date_closed = date_closed
        self.available = available
        self.username = username
            
    def __repr__(self):
        return '<Position {0}>'.format(self.position_id)


class PositionAppModel(db.Model):
    __tablename__ = 'positionapps'
    __table_args__ = {"schema":"jobmarket"}
    app_id = db.Column(db.Integer, primary_key=True)
    position_id = db.Column(db.Integer, 
        db.ForeignKey('jobmarket.positions.position_id'))
    username = db.Column(db.String(120), 
        db.ForeignKey('jobmarket.students.username'))
    db.UniqueConstraint('position_id', 'username', name='unique_app')
    offers = db.relationship('OfferModel', backref=db.backref('positionapps'),
                                lazy='dynamic')
    
    def __init__(self, app_id=None,
                position_id=None,
                username=None):

        self.app_id = app_id
        self.position_id = position_id
        self.username = username

    def __repr__(self):
        return '<Application {0}>'.format(self.app_id)


class OfferModel(db.Model):
    'the offer is tied to the application as a one-to-one'
    __tablename__ = 'offers'
    __table_args__ = {"schema":"jobmarket"}
    offer_id = db.Column(db.Integer, primary_key=True)
    app_id = db.Column(db.Integer, 
        db.ForeignKey('jobmarket.positionapps.app_id'))
    offer_made = db.Column(db.String(120))
    offer_date = db.Column(db.Date)
    response = db.Column(db.String(120))
    response_date = db.Column(db.Date)
    available = db.Column(db.String(120))
    
    def __init__(self, offer_id=offer_id, app_id=None,
                offer_made=None, offer_date=None,
                response=None, response_date=None,
                available=None):
        self.offer_id = offer_id
        self.app_id = app_id
        self.offer_made = offer_made
        self.offer_date = offer_date
        self.response = response
        self.response_date = response_date
        self.available = available
        
    def __repr__(self):
        return '<Application {0}>'.format(self.app_id)
