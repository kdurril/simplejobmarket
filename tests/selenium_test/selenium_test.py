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