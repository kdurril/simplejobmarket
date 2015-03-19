#Class based Selenium webdriver
#Web Driver for Student Specialization Evaluation
# extract student's courses from MEGS
# convert courses to list
# evaluate list with Specialization eval tools

#non standard library imports
from selenium import webdriver
from BeautifulSoup import BeautifulSoup

#standard library imports
import csv
import codecs
from datetime import date
from os import path, mkdir
import time
import getpass
import shutil

class DirectoryDriver(webdriver.Firefox):

    def __init__(self):
        webdriver.Firefox.__init__(self)
        self.register = "http://127.0.0.1:5000/register"
        self.login = "http://127.0.0.1:5000/login"
        #self.dst_path = None
        #self.src_path = None
        #self.files = None
        
        pass     

    def apra_start(self):
        self.get("127.0.0.1:5000/register")

    def register(self):
        "register for app"
        "use csv dict reader to register"
        with open("supervisors.csv", "r+b") as directory:
            supervisors = csv.DictReader(directory, delimiter=',')
            for x in supervisors:
                inputusername = self.find_element_by_name('username')
                inputpassword = self.find_element_by_name('password')
                inputpasswordconfirm = self.find_element_by_name('confirm')
                inputrole_id = self.find_element_by_name('role_id')
                inputcreate = self.find_element_by_xpath('//input[@value="create"]')
                inputusername.send_keys(x['username'])
                inputpassword.send_keys(x['password'])
                inputpasswordconfirm.send_keys(x['password'])
                inputrole_id.clear()
                inputrole_id.send_keys(x['role_id'])
                inputcreate.click()
                self.get("http://127.0.0.1:5000/register")

    def log_in(self):
        "log into the app"
        "use csv dict reader to log in"
        #Find fields and input credentials
        self.get("http://127.0.0.1:5000/login")
        with open("supervisors.csv", "r+b") as directory:
            supervisors = csv.DictReader(directory, delimiter=',')
            for x in supervisors:
                inputusername = self.find_element_by_name('username')
                inputpassword = self.find_element_by_name('password')
                inputlogin = self.find_element_by_xpath('//input[@value="login"]')
                inputout = self.find_element_by_xpath('//input[@value="logout"]')
                inputusername.send_keys(x['username'])
                inputpassword.send_keys(x['password'])
                inputlogin.click()
                self.get("http://127.0.0.1:5000/login")
                inputlogout.click()
                self.get("http://127.0.0.1:5000/login")


        inputname.send_keys(username)
        inputpassword.send_keys(password)
        time.sleep(2)



        inputsend = self.find_element_by_name('submit')
        inputsend.click()


    def create_poisition(self):
        self.get("127.0.0.1:5000/positions")
        pass

    def apply_to_position(self):
        self.get("127.0.0.1:5000/positions")
        pass

    def offer_position(self):
        self.get("127.0.0.1:5000/offers")
        pass

    def accept_position(self):


    def set_program(self):
        self.get('https://apra.umd.edu/login/programOrDepartment.jsp')
        get_value = self.find_element_by_name("program")
        get_value.find_element_by_xpath('//option[@value="MAPO"]')
        get_value.click()
        inputsend = self.find_element_by_xpath('//input[@type="submit"]')
        inputsend.click()
    
    
    def get_stat(self, path, today_sem="201501"):
        ##Get the directory list of all students in MEGS 
        
        path = self.today_dir

        time.sleep(1)
        self.get('https://apra.umd.edu/process.ece?action=showPage')
        time.sleep(1)
        self.get('https://apra.umd.edu/megs/stats/')
        time.sleep(5)
        self.get('https://apra.umd.edu/megs/stats/process.ece?action=showPage&page=main_stats_students.jsp')


        stat_select = ['program_ALL', 'sem_'+self.today_sem, 'checkbox_other_10']

        for item in stat_select:
            getlabel = self.find_element_by_name(item)
            getlabel.click()

        inputsend = self.find_element_by_xpath('//input[@type="submit"]')
        inputsend.click()
        time.sleep(30)

        source = self.page_source.encode('utf-8')
        nobr = self.find_elements_by_tag_name('nobr')
        
        with open(path+"/directory_tab.csv", "a+b") as directory:
            directory.write('''Last_name,first_name,middle_name,UID,sem,email,birthdate,major,program_code,advisor,street1,street2,street3,\city,state,zip,country,\degree_name,GRE_v,GRE_a,GRE_q,GRE_v_percentile,GRE_a_percentile,GRE_q_percentile,rating,TWE,TOEFL,GMAT,MAT_Miller,MAT_New_Miller_New_Score_range,LSAT,Certification,Special_Program,GRE_Subject_Score,GRE_Subject_Percentile,GRE_Subject_Name,Dept_Admission_Dec,GS_Admission_Dec,Dept_provision_codes,GS_provision_codes,GPA_undergrad,Home_Phone,Work_Phone,Is_International,ASF_Submit,Recommendation_1_Name,Recommendation_1_Received,Recommendation_2_Name,Recommendation_2_Received,Recommendation_3_Name,Recommendation_3_Received,Local_address_street1,Local_address_street2,Local_address_street3,Local_address_city,Local_address_state,Local_address_zip,Local_address_country,Num_Publications,Last_Undergrad_Univ_code,Last_Undergrad_Univs_Tier,Last_Undergrad_Univ_Long_Name,Last_Undergrad_Univ_ASF-entered_GPA,Last_Undergrad_Univ_ASF-entered_Major_Department,Last_Undergrad_Univ_Transcript_Received,Last_Graduate_Univ_code,Last_Graduate_Univs_Tier,Last_Graduate_Univ_Long_Name,Last_Graduate_Univ_ASF-entered_GPA,Last_Graduate_Univ_ASF-entered_Major_Department,Last_Graduate_Transcript_Received,Research_Interest_1,Research_Interest_2,Research_Interest_3,Research_Interest_4,visa,sex,race,citizenship,Interview_Audition_Scheduled_Date,Interview_Audition_Scheduled_Location,Interview_Audition_Primary_Request_Date,Interview_Audition_Secondary_Request_Date,ASF_Checkbox,ASF_TextBox_1,ASF_TextBox_2,ASF_TextBox_3,ASF_TextBox_4,ASF_TextBox_5,Minor,(For_students_only_Hometown),(For_students_only_Hobbies),(For_students_only_Buckley_code),Birthday_(birthdate_with_no_year),Faculty_Evaluator_1_name,Faculty_Evaluator_1_rank,Faculty_Evaluator_2_name,Faculty_Evaluator_2_rank,Faculty_Evaluator_3_name,Faculty_Evaluator_3_rank,Faculty_Evaluator_4_name,Faculty_Evaluator_4_rank,Faculty_Evaluator_5_name,Faculty_Evaluator_5_rank,Faculty_Evaluator_6_name,Faculty_Evaluator_6_rank,Faculty_Evaluator_7_name,Faculty_Evaluator_7_rank,Requested_Financial_Aid,Financial_Aid_this_sem_1_Semester,Financial_Aid_this_sem_1_Department_offering,Financial_Aid_this_sem_1_PHR_ID,Financial_Aid_this_sem_1_Type,Financial_Aid_this_sem_2_Semester,Financial_Aid_this_sem_2_Department_offering,Financial_Aid_this_sem_2_PHR_ID,Financial_Aid_this_sem_2_Type,forFuture1,forFuture2,forFuture3,forFuture4,forFuture5,forFuture6,forFuture7,forFuture8,forFuture9,forFuture10,forFuture11,forFuture12,forFuture13,forFuture14,forFuture15,forFuture16,forFuture17,forFuture18,forFuture19,forFuture20\n'''.encode('utf8'))
            for x in nobr[1:]:
                if len(x.text) > 2:
                    directory.write(x.text.encode('utf-8')+'\n')

    def get_UID(self, path):
    #strip the UIDs from the directory list
        path=self.today_dir
        with open(path+"/directory_tab.csv", "r+b") as directory:
            sReader = csv.DictReader(directory, delimiter=',')
            UIDlist = [x['UID'] for x in sReader if x['UID'].isdigit()]
        self.uidlist = UIDlist
        return UIDlist