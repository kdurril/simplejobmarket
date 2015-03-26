#GA Process 
#Views
#-*- coding: utf-8 -*-
#http://flask.pocoo.org/docs/views/ Method Based Dispatching

from simplejobmarket import app

from flask import render_template, redirect, url_for, flash


from flask.views import MethodView

from simplejobmarket.models import  UserModel,\
                                    StudentModel,\
                                    SupervisorModel,\
                                    PositionModel,\
                                    PositionAppModel,\
                                    OfferModel,\
                                    ResponseModel

from simplejobmarket.forms import   UserForm,\
                                    RegistrationForm,\
                                    StudentForm,\
                                    SupervisorForm,\
                                    PositionForm,\
                                    ApplicationForm,\
                                    OfferForm,\
                                    OfferYes,\
                                    OfferNo,\
                                    ResponseForm


from simplejobmarket.models import db

from flask.ext.login import login_user, logout_user, login_required, current_user
import datetime



#db.sessionmaker

app.secret_key = 'hard to guess string' #os.environ.get('SECRET')

@app.route('/')
def hello_world():
    return 'Hello World!'

def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = UserModel(username=form.username.data)
        user.password = form.password.data
        user.role_id = form.role_id.data
        #user.id = None
        db.session.add(user)
        db.session.commit()
        flash('User added, you can login')
        return redirect(url_for('student_view'))
    return render_template('register.html', form=form)

#app.add_url_rule('/register/', view_func=register, methods=['GET','POST'])

def login():
    form = UserForm()
    if form.validate_on_submit():
        user = UserModel.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for('student_view'))
        flash('Invalid username or password.')
    return render_template('login.html', form=form)

def logout():
    logout_user()
    return redirect(url_for('student_view'))


def dashboard(username):
    'Display of most useful data'
    'Offer accepted, offers declined, positions available'
    offers = OfferModel().filter_by(username=current_user.username)
    post = PositionModel()
    positionapps = PositionAppModel()
    app_review = post.query.filter(\
            PositionModel().username==current_user.username)\
            .join(PositionAppModel)\
            .join(StudentModel)
    

    return render_template('dashboard_student.html', offers=offers, positions=positions)

class AuthView(MethodView):
    'This takes UserModel, UserForms'
    def post(self):
        user = UserModel()
        form = AuthForm()
        if form.validate_on_submit():
            #USE Authentication HERE
            form.populate_obj(user)
            return redirect(url_for('auth.html'))

        return render_template('auth.html')

    def get(self):
        user = UserModel()
        form = UserForm(obj=user)
        return render_template('auth.html', form=form)

class StudentView(MethodView):

    def post(self):
        "create new student record, http://flask.pocoo.org/snippets/63/ for easy WTforms redirect"
        student = StudentModel()
        form = StudentForm()
        student_update = student.query.all()

        if form.validate_on_submit():
            form.populate_obj(student)
            student.username = current_user.username
            db.session.add(student)
            db.session.commit()
            return redirect('/')
            
        return render_template('student_review.html', student_list=student_update, form=form)

    def put(self, student_id):
        "edit student record"
        "http://wtforms.simplecodes.com/docs/0.6.1/forms.html#wtforms.form.Form.populate_obj"
        student = StudentModel()
        student_update = student.query.get(username)
        current_student = [student_update]
        form = StudentForm()
        form.populate_obj(student_update)

        if form.validate_on_submit():
            form.populate_obj(student_update)
            #student_update.student_uid=form.student_uid.data
            #student_update.name_last=form.name_last.data
            #student_update.name_first=form.name_first.data
            #student_update.email=form.email.data
            #student_update.phone=form.phone.data
            #student_update.major=form.major.data
            #student_update.program_code=form.program_code.data
            #student_update.sem_begin=form.sem_begin.data
            #student_update.graduation_expected=form.graduation_expected.data
            #student_update.credit_fall=form.credit_fall.data
            #student_update.credit_spring=form.credit_spring.data 
            #student_update.request_fall=form.request_fall.data
            #student_update.request_spring=form.request_spring.data
            db.session.add(student_update)
            db.session.commit()
            return redirect('/')
        return redirect('/')
        #return render_template('student_update.html', student_id=student_id, student_list=current_update, form=form)


    def delete(self, username):
        "delete student record"
        student = StudentModel()
        student_delete = student.query.get(username)
        db.session.delete(student_delete)
        db.commit()

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

                
            return render_template('student_update.html', student_id=student_id, 
                student_list=[current_student], form=form)

class SupervisorView(MethodView):
    def post(self):
        "create supervisor record"
        supervisor = SupervisorModel()
        form = SupervisorForm()
        if form.validate():
            form.populate_obj(supervisor)
            supervisor.username = current_user.username
            db.session.add(supervisor)
            db.session.commit()
            return redirect(url_for('supervisors'))
        

    def put(self, supervisor_id):
        "edit supervisor record"
        pass

    def delete(self, supervisor_id):
        "delete supervisor record"
        supervisor = SupervisorModel()
        supervisor_delete = supervisor.delete(supervisor_id)
        db.session.delete(supervisor_delete)
        db.session.commit()
        pass

    def get(self):
        "review supervisor record"
        supervisor = SupervisorModel()
        supervisor = supervisor.query.all()
        form = SupervisorForm()
        #supervisor can only view his own record
        return render_template('supervisor_review.html', supervisor_list=supervisor, form=form)

class PositionView(MethodView):

    def post(self):
        "create position record"
        position = PositionModel()
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
            position.username = current_user.username
            
            db.session.add(position)
            db.session.commit()
            return redirect(url_for('student_view'))

        return redirect('/')
            
        

    def put(self):
        "edit position record"
        pass

    def delete(self, position_id):
        "delete position record"
        pass

    def get(self, position_id=None):
        "review position record"
        position = PositionModel()
        position_all = position.query.all()
        applications = PositionAppModel()
        app_submitted = applications.query.filter_by(username=current_user.username)
        exclude_app = [str(x.position_id) for x in app_submitted]
        pagination = position.query.paginate(1,1)
        form = PositionForm()
        #if user is owner, decorate to allow put and delete

        if current_user.role_id == 2:
            if position_id is None:
                # return a list of users
                position_user = position.query.filter_by(username=current_user.username)
                pagination = position.query.paginate(1,1)
                return render_template('position_pages.html',\
                position_id=position_id, position_list=position_user,\
                pagination=pagination, form=form)
            else:
                position_one = position.query.get(position_id)
                return render_template('position_pages.html',\
                        position_id=position_id, position_list=[position_one],\
                        pagination=pagination, app_submitted=app_submitted,\
                        exclude_app=exclude_app, form=form)
        else:
            if position_id is None:
                # return a list of users
                pagination = position.query.paginate(1,1)
                return render_template('position_pages.html',\
                position_id=position_id, position_list=position_all,\
                pagination=pagination, form=form)
            else:
                position_one = position.query.get(position_id)
                return render_template('position_pages.html',\
                        position_id=position_id, position_list=[position_one],\
                        pagination=pagination, app_submitted=app_submitted,\
                        exclude_app=exclude_app, form=form)

#Move to urls
#app.add_url_rule('/positions/', view_func=PositionView.as_view('positions'), template_name='position_review.html')
#this view must be restricted to the positon owner/supervisor
#app.add_url_rule('/positions/<int:position_id>', view_func=position_view,
#                 methods=['GET', 'PUT', 'DELETE'])

class ApplicationView(MethodView):
    def post(self,position_id):
        "create application record"
        applications = PositionAppModel()
        form = ApplicationForm()

        if form.validate():
            form.populate_obj(applications)
            '''applications(form.app_id.data,
            form.student_id.data,
            form.position_id.data
            )'''
            applications.username = current_user.username
            applications.position_id = position_id
            db.session.add(applications)
            #try:
            #db.session.commit()
            #except:
            #    flash('Your application was not accepted')
            #    return redirect(url_for('position_view'))
            flash('Thank you for applying')
            return redirect(url_for('student_view'))
            


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
            return render_template('position_review.html', form=form)
        else:
            # expose a single user
            pass
        
#Move to urls
#app.add_url_rule('/application/', view_func=ApplicationView.as_view('application'))

class OfferView(MethodView):
    def post(self):
        "create new offer"
        offers = OfferModel()
        form = OfferForm()
        form_yes = OfferYes()
        form_no = OfferNo()

        if form_yes.validate():
            form_yes.populate_obj(offers)
            db.session.add(offers)
            db.session.commit()
            flash('Offered')
            return redirect(url_for('student_view'))

        if form_no.validate():
            form_no.populate_obj(offers)
            db.session.add(offers)
            db.session.commit()
            flash('Declined')
            return redirect(url_for('student_view'))
            
    def put(self, app_id):
        "response or edit offer"
        #MOVE THIS TO ANOTHER TABLE
        offers = OfferModel()

        if current_user.role_id == 2:
            #Student response
            form = ResponseForm()
            if form.validate():
                form.populate_obj(offers)
                db.session.add(offers)
                db.session.commit()
                flash('Response Sent')
            pass

        #DON'T ALLOW OFFER REVISION, JUST DELETION
        #if current_user.role_id == 2:
        #    #Supervisor Update
        #    form = OfferForm()
        #    if form.validate():
        #        form.populate_obj(offers)
        #        db.session.add(offers)
        #        db.session.commit()
        #        flash('Offer Updated')
        #    pass

    def delete(self, app_id):
        "delete offer"
        pass

    def get(self, app_id=None):
        "review offer"
        offer = OfferModel()
        offer = offer.query.all()
        form = OfferForm()
        form_yes = OfferYes()
        form_no = OfferNo()
        post = PositionModel()
        student_app = PositionAppModel()
        
        position = post.query.filter_by(username=current_user.username).all()
        #if user is owner, decorate to allow put and delete
        #if offer_id is owner:
            # return a list of users
        #    pass
        #if user is applicant offered position, allow view of its offers
        #elif offer_id is applicant:
        if current_user.role_id == 2:
            # expose a single user
            app_review = student_app.query\
            .join(StudentModel)\
            .join(PositionModel).filter_by(username=current_user.username)
            app_review_all = app_review.all()

            return render_template('offer_review.html', offer_list=offer,\
                app_review=app_review, app_review_all=app_review_all,\
                position=position, student_app=PositionAppModel(),\
                form=form, form_yes=form_yes, form_no=form_no)

        else:
            redirect(url_for('position_view'))

class OfferResponse(MethodView):

    def post(self, username=None):
        form = ResponseForm()
        response = ResponseModel()
        if form.validate():
            #form.populate_obj(offer)
            response.offer_id = form.offer_id.data
            response.response = form.response.data
            response.available = form.available.data
            response.response_date = datetime.datetime.now()
            db.session.add(response)
            db.session.commit()
            flash('Submission Received')
            return redirect(url_for('student_view'))

    def put(self):
        "put is not allowed"
        pass

    def delete(self):
        "delete is not allowed"
        pass

    def get(self, username=None):
        offer = OfferModel()
        application = PositionAppModel()
        position = PositionModel()
        form = ResponseForm()
        if current_user.username == username:
            #get offers based on
            #app_id
            #username
            #offer_user = offer.query.filter(PositionAppModel().username == current_user.username)\
            offer_user = offer.query.join(PositionAppModel)\
                                    .join(PositionModel)\
                                    .filter(PositionAppModel.username==current_user.username)\
                                    .all()
            #offer_user = application.query.filter_by(username=username)
            #.query.filter(\
            #    PositionAppModel().username==current_user.username)#\
                #.join(OfferModel)\
                #.join(PositionModel)
            position_alias = db.aliased(PositionAppModel)
            #a = (position_alias, offer.usename == user_alias.username)
            #(position_alias, position_alias.username == current_user.username)
            # position.query.filter_by(username=current_user.username)
            offer_test = offer.query.join(PositionAppModel)\
                                    .join(PositionModel)\
                                    .filter(PositionAppModel.username==current_user.username)\
                                    .all()

            return render_template('offer_response.html', form=form,\
             offer_user=offer_user, offer_test=offer_test,\
              offer=offer, application=application, position=position)

        return redirect(url_for('student_view'))