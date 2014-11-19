#SIMPLE JOB MARKET

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://kdurril:4054756umd@localhost/postgres'
db = SQLAlchemy(app)



class StudentsModel(db.Model):
    __tablename__ = 'students'
    __table_args__ = {"schema":"jobmarket"}
    
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
    request201408 = db.Column(db.String(120))
    request201501 = db.Column(db.String(120))
    #position_apps = db.relationship("PositionApps", backref='Students',
    #                            lazy='dynamic')
    
    def __init__(self, student_uid=None, name_last=None,
                name_first=None, email=None,
                phone=None, major=None,
                program_code=None, sem_begin=None,
                graduation_expected=None, credit_fall=None,
                credit_spring=None, request201408=None,
                request201501=None):
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
        self.request201408 = request201408
        self.request201501 = request201501
        
    def __repr__(self):
        return '<Student {0}>'.format(self.student_uid)


class SupervisorsModel(db.Model):
    __tablename__ = 'supervisors'
    __table_args__ = {"schema":"jobmarket"}
    supervisor_id = db.Column(db.Integer, primary_key=True)
    name_last = db.Column(db.String(120))
    name_first = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    email = db.Column(db.String(120))
    room = db.Column(db.String(120))
    center = db.Column(db.String(120))
    position = db.relationship("PositionsModel", backref='supervisors',
                                lazy='dynamic')

    def __init__(self, supervisor_id=None, 
                name_last=None, name_first=None,
                phone=None, email=None,
                room=None, center=None):
        self.supervisor_id = supervisor_id
        self.name_last = name_last
        self.name_frst = name_first
        self.phone = phone
        self.email = email
        self.room = room
        self.center = center
        
    def __repr__(self):
        return '<Supservisor {0}>'.format(self.supervisor_id)

class PositionsModel(db.Model):
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
    available = db.Column(db.String(120))
    supervisor_id = db.Column(db.Integer, db.ForeignKey('SupervisorsModel.supervisor_id'), nullable=False)
    supervisor = db.relationship("SupervisorsModel", primaryjoin=PositionsModel.supervisor_id == SupervisorsModel.supervisor_id, viewonly=True)
    #position_app = db.relationship('PositionApps', backref='Positions',
    #                                lazy='dynamic')

    def __init__(self, position_id=None,
                title=None, work_group=None, position_type=None,
                course=None, program_min=None, program_std=None,
                position_overview=None, primary_duties=None,
                necessary_skill=None, preferred_skill=None,
                date_open=None, date_closed=None,
                available=None, supervisor_id=None):
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
        self.supervisor_id = supervisor_id
            
    def __repr__(self):
        return '<Position {0}>'.format(self.position_id)

other = '''
class PositionApps(db.Model):
    __tablename__ = 'positionapps'
    __table_args__ = {"schema":"jobmarket"}
    app_id = db.Column(db.Integer)
    position_id = db.Column(db.Integer, db.ForeignKey('Positions.position_id'), primary_key=True)
    student_uid = db.Column(db.String(120), db.ForeignKey('Students.student_uid'), primary_key=True)
    positions = db.relationship('Positions', secondaryjoin=position_id == Positions.position_id)
    students = db.relationship('Students', primaryjoin=student_uid == Students.student_uid)
    
    offers = db.relationship('Offers', backref='PositionApps',
                                lazy='dynamic')
    db.UniqueConstraint('position_id', 'student_uid', name='unique_app')
    #students = db.relationship('Students') #, backref="positionapps"
    #offers = db.relationship('Offers') 
        #,backref=db.backref('positionapps', lazy='joined', uselist=False),
        #lazy='dynamic')

    def __init__(self, app_id=None,
                position_id=None,
                student_id=None
                ):

        self.app_id = app_id
        self.position_id = position_id
        self.student_uid = student_uid

    def __repr__(self):
        return '<Application {0}>'.format(self.app_id)

class Offers(db.Model):
    __tablename__ = 'offers'
    __table_args__ = {"schema":"jobmarket"}
    offer_id = db.Column(db.Integer, primary_key=True)
    app_id = db.Column(db.Integer, db.ForeignKey('PositionApps.app_id'))
    offer_made = db.Column(db.String(120))
    offer_date = db.Column(db.String(120))
    response = db.Column(db.String(120))
    response_date = db.Column(db.String(120))
    available = db.Column(db.String(120))
    position_apps = db.relationship('PositionApps',primaryjoin=app_id == PositionApps.app_id)

    def __init__(self, offer_id=None, app_id=None,
                offer_made=None, offer_date=None,
                response=None, response_date=None,
                available=None):
        self.offer_id = offer_id
        self.app_id = app_id
        self.offer_made = offerMade
        self.offer_date = offer_date
        self.response = response
        self.response_date = response_date
        self.available = available

    def __repr__(self):
        return '<Application {0}>'.format(self.app_id)

'''
