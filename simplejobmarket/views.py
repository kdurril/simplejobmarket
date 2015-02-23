#GA Process 
#Views
#-*- coding: utf-8 -*-
#http://flask.pocoo.org/docs/views/ Method Based Dispatching

from simplejobmarket import app

from flask import render_template, redirect, url_for

from flask.views import MethodView

from simplejobmarket.models import StudentModel,\
                                    SupervisorModel,\
                                    PositionModel,\
                                    PositionAppModel,\
                                    OfferModel

from simplejobmarket.forms import StudentForm,\
                                    SupervisorForm,\
                                    PositionForm,\
                                    ApplicationForm,\
                                    OfferForm

from simplejobmarket.models import db

db.sessionmaker


app.secret_key = 'hard to guess string' #os.environ.get('SECRET')

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/bros/')
def student():
    "review student record"

    student = StudentModel()
    student = student.query.all()
    form = StudentForm()

    
    return render_template('student_review.html', student_list=student, form=form)

@app.route('/bros/<int:student_id>', methods=['GET','PUT'])
def student_by_id(student_id):
    student = StudentModel()
    #need an object and a list containing object for template
    student = student.query.get(student_id)
    current_student = student
    form = StudentForm(obj=student)
                        
    return render_template('student_update.html', student_id=student_id, student_list=[current_student], form=form)

class StudentTest(MethodView):
    def post(self, student_id=None):
        student = StudentModel()
        form = StudentForm()
        if student_id == None:
            if form.validate_on_submit():
                form.populate_obj(student)
                db.session.add(student)
                db.session.commit()
                return redirect('student_test')
        else:
            if form.validate_on_submit():
                student_by_id = student.query.get(student_id) 
                
                student_by_id.studentUid = form.studentUid.data
                student_by_id.nameLast = form.nameLast.data
                student_by_id.nameFirst = form.nameFirst.data
                student_by_id.email = form.email.data
                student_by_id.phone = form.phone.data
                student_by_id.major = form.major.data
                student_by_id.programCode = form.programCode.data
                student_by_id.semBegin = form.semBegin.data
                student_by_id.graduationExpected = form.graduationExpected.data
                student_by_id.creditFall = form.creditFall.data
                student_by_id.creditSpring = form.creditSpring.data 
                student_by_id.request201408 = form.request201408.data
                student_by_id.request201501 = form.request201501.data
                db.session.commit()
                return redirect('student_test')

        return redirect('/')

    def put(self, student_id):
        student = StudentModel()
        student_by_id = student.query.get(student_id)
        form = StudentForm()
        if form.validate_on_submit():
            form.populate_obj(student)
            db.update(student_by_id)
            db.session.commit()
            return redirect('student_test')
        return redirect('/')
        

    def delete(self, student_id):

        student = StudentModel()
        student_by_id = student.query.get(student_id)
        db.delete(student_by_id)
        db.session.commit()
        return redirect('student_test')
        
    def get(self, student_id=None):

        if student_id == None:
            student = StudentModel()
            student_list = student.query.all()
            form = StudentForm()
            return render_template('student_test.html', student_list=student_list, form=form)
        else:
            student = StudentModel()
            student_list = student.query.get(student_id)
            form = StudentForm(obj=student_list)
            return render_template('student_test_update.html', student_id=student_id, student_list=[student_list], form=form)

student_test = StudentTest.as_view('student_test')
student_put = StudentTest.as_view('student_put')

app.add_url_rule('/student_test/',\
    view_func=student_test,\
    methods=['GET','POST'])

app.add_url_rule('/student_test/<int:student_id>',\
    view_func=student_put,\
    methods=['GET', 'PUT', 'DELETE'])



class StudentView(MethodView):

    def post(self):
        "create new student record, http://flask.pocoo.org/snippets/63/ for easy WTforms redirect"
        student = StudentModel()
        form = StudentForm()
        student_update = student.query.all()

        if form.validate_on_submit():
            form.populate_obj(student)
            '''student = StudentModel(
            None,
            form.studentUid.data,
            form.nameLast.data,
            form.nameFirst.data,
            form.email.data,
            form.phone.data,
            form.major.data,
            form.programCode.data,
            form.semBegin.data,
            form.graduationExpected.data,
            form.creditFall.data,
            form.creditSpring.data, 
            form.request201408.data,
            form.request201501.data
                )'''
            db.session.add(student)
            db.session.commit()
            return redirect('/')
            
            
        return render_template('student_review.html', student_list=student_update, form=form)

    def put(self, student_id):
        "edit student record"
        "http://wtforms.simplecodes.com/docs/0.6.1/forms.html#wtforms.form.Form.populate_obj"
        student = StudentModel()
        student_update = student.query.get(student_id)
        current_student = [student_update]
        form = StudentForm()
        
        student_update.student_uid=form.student_uid.data
        student_update.name_last=form.name_last.data
        student_update.name_first=form.name_first.data
        student_update.email=form.email.data
        student_update.phone=form.phone.data
        student_update.major=form.major.data
        student_update.program_code=form.program_code.data
        student_update.sem_begin=form.sem_begin.data
        student_update.graduation_expected=form.graduation_expected.data
        student_update.credit_fall=form.credit_fall.data
        student_update.credit_spring=form.credit_spring.data 
        student_update.request201408=form.request201408.data
        student_update.request201501=form.request201501.data

        db.session.commit()

        if form.validate_on_submit():
            
            student_update.student_uid=form.student_uid.data
            student_update.name_last=form.name_last.data
            student_update.name_first=form.name_first.data
            student_update.email=form.email.data
            student_update.phone=form.phone.data
            student_update.major=form.major.data
            student_update.program_code=form.program_code.data
            student_update.sem_begin=form.sem_begin.data
            student_update.graduation_expected=form.graduation_expected.data
            student_update.credit_fall=form.credit_fall.data
            student_update.credit_spring=form.credit_spring.data 
            student_update.request201408=form.request201408.data
            student_update.request201501=form.request201501.data

            db.session.commit()
            return redirect('/')
        return redirect('/')
        #return render_template('student_update.html', student_id=student_id, student_list=current_update, form=form)


    def delete(self, student_id):
        "delete student record"
        student = StudentModel()
        student_delete = student.query.get(student_uid)
        db.delete(student_delete)

        return redirect(url_for('student_view'))

    def get(self, student_id=None):
        "review student record"
        if student_id is None:
            student = StudentModel()
            student_list = student.query.all()
            form = StudentForm()
            
            return render_template('student_review.html', student_list=student_list, form=form)
        else:
            student = StudentModel()
            #need an object and a list containing object for template
            #

            student = student.query.get(student_uid)
            current_student = student
            form = StudentForm(obj=student)
            #student.populate_obj(form)
            #form.studentUid.data = student.studentUid 
            #form.nameLast.data = student.nameLast
            #form.nameFirst.data = student.nameFirst
            #form.email.data = student.email
            #form.phone.data = student.phone 
            #form.major.data = student.major 
            #form.programCode.data = student.programCode 
            #form.semBegin.data = student.semBegin
            #form.graduationExpected.data = student.graduationExpected
            #form.creditFall.data = student.creditFall
            #form.creditSpring.data = student.creditSpring
            #form.request201408.data = student.request201408
            #form.request201501.data = student.request201501
                
            return render_template('student_update.html', student_id=student_id, 
                student_list=[current_student], form=form)


        #return render_template('student_reveiw.html', students=students)
        

        #def show_user(username):
        #    student = StudentView.query.filter_by(student=username).first_or_404()
        #    return render_template('show_user.html', user=user)
        
        
#Move to urls
#app.add_url_rule('/students/', view_func=StudentView.as_view('students'),\
#    template_name='student_review.html', methods=['GET',])
#app.add_url_rule('/students/add', view_func=StudentView.as_view('students'),\
#    template_name='student_review.html', methods=['POST',])
#app.add_url_rule('/students/<int: student_id>', view_func=StudentView.as_view('students'),\
#    template_name='student_review.html', methods=['GET', 'PUT', 'DELETE'])


class SupervisorView(MethodView):
    def post(self):
        "create supervisor record"
        supervisor = SupervisorModel()
        form = SupervisorForm()
        if form.validate():
            form.populate_obj(supervisor)
            '''supervisor(
            10,
            form.nameLast.data,
            form.nameFirst.data,
            form.phone.data,
            form.email.data,
            form.room.data,
            form.center.data
            )'''
            db.session.add(supervisor)
            db.session.commit()
        return redirect('/')
        

    def put(self, supervisor_id):
        "edit supervisor record"
        pass

    def delete(self, supervisor_id):
        "delete supervisor record"
        supervisor = SupervisorModel()
        supervisor = supervisor.delete(supervisor_id)
        pass

    def get(self):
        "review supervisor record"
        supervisor = SupervisorModel()
        supervisor = supervisor.query.all()
        form = SupervisorForm()
        #supervisor can only view his own record
        return render_template('supervisor_review.html', supervisor_list=supervisor, form=form)
#Move to urls
#app.add_url_rule('/supervisors/', view_func=SupervisorView.as_view('supervisors'), template_name='supervisor_review.html')

class PositionView(MethodView):

    def post(self):
        "create position record"
        position = PostionModel()
        form = PositionForm()
        if form.validate():
            form.populate_obj(position)
            '''position(
            form.position_id.data,
            form.title.data,
            form.workGroup.data,
            form.position_type.data,
            form.course.data,
            form.programMin.data,
            form.programStd.data,
            form.positionOverview.data,
            form.primaryDuties.data,
            form.necessarySkill.data,
            form.preferredSkill.data,
            form.dateOpen.data,
            form.dateClosed.data,
            form.available.data,
            form.supervisor_id.data
            )'''
            return position
            db.session.add(position)
            bd_session.commit()
        

    def put(self):
        "edit position record"
        pass

    def delete(self, position_id):
        "delete position record"
        pass

    def get(self, position_id=None):
        "review position record"
        position = PositionModel()
        position = position.query.all()
        form = PositionForm()
        #if user is owner, decorate to allow put and delete
        if position_id is None:
            # return a list of users
            return render_template('position_review.html', position_list=position, form=form)
        else:
            # expose a single user
            pass

#Move to urls
#app.add_url_rule('/positions/', view_func=PositionView.as_view('positions'), template_name='position_review.html')
#this view must be restricted to the positon owner/supervisor
#app.add_url_rule('/positions/<int:position_id>', view_func=position_view,
#                 methods=['GET', 'PUT', 'DELETE'])

class ApplicationView(MethodView):
    def post(self, position_id):
        "create application record"
        applications = PositionAppModel()
        form = ApplicationForm(request.form)
        if form.validate():
            form.populate_obj(applications)
            '''applications(form.app_id.data,
            form.student_id.data,
            form.position_id.data
            )'''
            return application
            db.session.add(application)
            db.session.commit()


    def put(self, position_id):
        "edit application record"
        pass

    def delete(self, position_id):
        "delete application record"
        pass

    def get(self, offer_id=None):
        "review application record"
        form = ApplicationForm()
        #if user is owner, decorate to allow put and delete
        if offer_id is None:
            # return a list of users
            return render_template('position_review.html', position_list=offer, form=form)
        else:
            # expose a single user
            pass
        
#Move to urls
#app.add_url_rule('/application/', view_func=ApplicationView.as_view('application'))

class OfferView(MethodView):
    def post(self, app_id):
        "create new offer"
        offers = OfferModel()
        form = OfferForm(request.form)
        if form.validate():
            form.populate_obj(offers)
            '''offers.offer_id = form.offer_id.data
            offers.app_id = form.app_id.data
            offers.offerMade = form.offerMade.data 
            offers.offer_date = form.offer_date.data 
            offers.response = form.response.data
            offers.response_date = form.response_date.data
            offers.available = form.available.data'''
            return offers
            db.app(offers)
            db.session.commit()

    def put(self, app_id):
        "edit offer"
        pass

    def delete(self, app_id):
        "delete offer"
        pass

    def get(self, app_id=None):
        "review offer"
        offer = OfferModel()
        offer = offer.query.all()
        form = SupervisorForm()
        
        #if user is owner, decorate to allow put and delete
        #if offer_id is owner:
            # return a list of users
        #    pass
        #if user is applicant offered position, allow view of its offers
        #elif offer_id is applicant:
            
        #    return render_template('offer_review.html', offer_list=offer, form=form)
        if app_id == None:
            # expose a single user
            return render_template('offer_review.html', offer_list=offer, form=form)

        else:
            redirect(url_for('position_view'))