from flask import Flask, current_app
from flaskapp.db_models import User
import unittest
from flask import request
import requests
from flaskapp import db

app = Flask(__name__)
with app.app_context(): db.create_all()



def db():
    users_in_db=[]

    users = User.query.all()
    for x in users:
        users_in_db.append(x.username)
    return users_in_db


class FlaskTest(unittest.TestCase):
    URL = 'http://127.0.0.1:5000/'
    DATA = dict(username='kingkong', email = 'kingkong@gmail.com', password = 'kingkong@gmail.com')
    #TEST_ROUTES
    #home
    def test_1_home(self):
        r = requests.get(FlaskTest.URL+'home')
        self.assertFalse(b'New Post' in r.content)

    #about
    def test_2_about(self):
        r = requests.get(FlaskTest.URL+'about')
        self.assertTrue(b'This is about page.' in r.content) 

    #register_FAILED
    def test_3_register_fail(self):
        r = requests.post(FlaskTest.URL+'signup', data = FlaskTest.DATA)
        self.assertTrue(b'That username is already taken!' in r.content) 

    
"""     #register_SUCCESS
    def test_4_register(self):
        r = requests.post(FlaskTest.URL+'signup', data = dict(username='king2kong', email = 'king2kong@gmail.com', password = 'king2kong@gmail.com', confirm_password = 'king2kong@gmail.com' ))
        if 'king2kong' in db():
            print('yes')
        else:
            print('no') """


""" #signin_FAIL
    def test_login(self):
        tester = current_app.test_client(self)
        tester.post('/signin', data = dict(email = 'kingkocng@gmail.com', password = 'kingkocng@gmail.com'),follow_redirects =True)
        response = tester.get( '/signin', follow_redirects = True)
        self.assertTrue(b'This website was built admist the Pandemic :)' in response.data)   

    #signin_SUCCESS
    def test_login(self):
        tester = current_app.test_client(self)
        response = tester.post('/signin', data = dict(email = 'kingkong@gmail.com', password = 'kingkong@gmail.com'), follow_redirects =True) 
       # self.assertIn(b'kingkongpost', response.data)
    
 
        #self.assertIn(b'Log In', response.data) """

if __name__ == '__main__':
    unittest.main()