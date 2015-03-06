#!/usr/bin/env python
#-*- coding: utf-8 -*-

from simplejobmarket import app
from simplejobmarket.views import AuthView, StudentView, SupervisorView,\
                                  PositionView, ApplicationView, OfferView,\
                                  register, login, logout 


#Authorization
auth_view = AuthView.as_view('auth')
app.add_url_rule('/auth/', view_func=auth_view, methods=['GET','POST'])

app.add_url_rule('/login/', view_func=login, methods=['GET','POST'])

app.add_url_rule('/logout/', view_func=logout, methods=['GET'])

app.add_url_rule('/register/', view_func=register, methods=['GET','POST'])

def supervisor_required(f):
    """Checks whether user is logged in or raises error 401."""
    def decorator(*args, **kwargs):
        if not current_user.role_id == 2:
            abort(401)
        return f(*args, **kwargs)
    return decorator


#Student
student_view = StudentView.as_view('student_view')
app.add_url_rule('/students/',\
	view_func=student_view,\
	methods=['GET','POST'])
app.add_url_rule('/students/',\
	view_func=student_view,\
	methods=['POST'])
app.add_url_rule('/students/<int:student_id>',\
	view_func=student_view,\
	methods=['GET','PUT', 'DELETE'])

#Supervisor
supervisor_view = SupervisorView.as_view('supervisors')
app.add_url_rule('/supervisors/',\
	view_func=supervisor_view,\
	methods=['GET',])
app.add_url_rule('/supervisors/',\
	view_func=supervisor_view,
	methods=['POST',])

app.add_url_rule('/supervisors/<int:supervisor_id>',\
	view_func=supervisor_view,\
	methods=['GET', 'PUT', 'DELETE'])

#Positions
position_view = PositionView.as_view('positions')
app.add_url_rule('/positions/',\
	view_func=position_view,\
	methods=['GET','POST'])
#this view must be restricted to the positon owner/supervisor
app.add_url_rule('/positions/<int:position_id>',\
	view_func=position_view,\
    methods=['GET', 'PUT', 'DELETE'])

#For review of applications for individual
application_view = ApplicationView.as_view('applications')
#app.add_url_rule('/applications/', view_func=application_view)
app.add_url_rule('/applications/<position_id>',\
	view_func=application_view,
	methods=['POST'])

#OFFER
offer_view = OfferView.as_view('offers')
app.add_url_rule('/offers/', view_func=offer_view, methods=['GET',])
app.add_url_rule('/offers/<int:offer_id>', view_func=offer_view,\
    methods=['GET', 'PUT', 'DELETE'])
