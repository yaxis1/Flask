from flaskapp.db_models import User
from flask import Flask, request
from flaskapp.db_models import User
import unittest, requests
from flaskapp import db, create_app
from flask_bcrypt import Bcrypt

#Initializing test app
app = create_app()

#with app.app_context():
db.app = create_app()

def db():
    users_in_db=[]
    users = User.query.all()
    for x in users:
        users_in_db.append(x.username + ':' + x.email + ':' + x.password)
    return users_in_db
print(db())

class FlaskTest(unittest.TestCase):
    URL = 'localhost:2103/'
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

        #self.assertTrue(b'Your account has been created, you can now login!' in r.content)      

""" #signin_FAIL
    def test_5_login(self):
        with requests.Session() as s:

            r = s.post(FlaskTest.URL+'signin', data = dict(email = 'king3kong@gmail.com', password = '1234567595' ,allow_redirects=True))
            #print(r.text)
            self.assertEqual(r.status_code, 201)
            #self.assertTrue(b'login unsuccessful' in r.content)   """


"""    #register_SUCCESS
    def test_4_register(self):
        bcrypt = Bcrypt()
        with requests.Session() as s:
            hashed_password = bcrypt.generate_password_hash('king3kong@gmail.com').decode('utf-8')

            r = s.post(FlaskTest.URL+'signup', data = dict(username='king3kong', email = 'king3kong@gmail.com', password = '1234567595' ))
            print(r.text)
            self.assertEqual(r.status_code, 201)  """
""" 
    #signin_SUCCESS
    def test_login(self):
        tester = current_app.test_client(self)
        response = tester.post('/signin', data = dict(email = 'kingkong@gmail.com', password = 'kingkong@gmail.com'), follow_redirects =True) 
       # self.assertIn(b'kingkongpost', response.data)
    
 
        #self.assertIn(b'Log In', response.data)  """

if __name__ == '__main__':
    unittest.main()