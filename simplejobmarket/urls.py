from simplejobmarket import app
from simplejobmarket.views import StudentView, SupervisorView, PositionView, ApplicationView, OfferView 

student_view = StudentView.as_view('student_view')
app.add_url_rule('/students/',\
	view_func=student_view,\
	methods=['GET',])
app.add_url_rule('/students/',\
	view_func=student_view,\
	methods=['POST'])
app.add_url_rule('/students/<int:student_id>',\
	view_func=student_view,\
	methods=['GET','PUT', 'DELETE'])


#app.add_url_rule('/students/<int:student_id>/delete',\
#	view_func=student_view,\
#	methods=['DELETE'])

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
    #view_func=SupervisorView.as_view('supervisors')

#Move to urls
position_view = PositionView.as_view('positions')
app.add_url_rule('/positions/',\
	view_func=position_view,\
	methods=['GET',])
#this view must be restricted to the positon owner/supervisor
app.add_url_rule('/positions/<int:position_id>',\
	view_func=position_view,\
    methods=['GET', 'PUT', 'DELETE'])
#For review of applications for individual
application_view = ApplicationView.as_view('applications')
app.add_url_rule('/applications/', view_func=application_view)
#OFFER
offer_view = OfferView.as_view('offers')
app.add_url_rule('/offers/', view_func=offer_view, methods=['GET',])
app.add_url_rule('/offers/<int:offer_id>', view_func=offer_view,\
    methods=['GET', 'PUT', 'DELETE'])
