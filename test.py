from flaskapp.db_models import User
from flask import current_app
import unittest
from flask import request

def db():
    users_in_db=[]
    users = User.query.all()
    for x in users:
        users_in_db.append(x.username)
    return users_in_db

class FlaskTest(unittest.TestCase):
    #TEST_ROUTES
    #home
    def test_home(self):
        tester = current_app.test_client(self)
        response = tester.get('/home', content_type='html')
        self.assertFalse(b'New Post' in response.data)

    #about
    def test_about(self):
        tester = current_app.test_client(self)
        response = tester.get('/about', content_type='html')        
        self.assertTrue(b'This is about page.' in response.data)

    #register_FAILED
    def test_register_fail(self):
        tester = current_app.test_client(self)
        response = tester.post('/signup', data = dict(username='kingkong', email = 'kingkong@gmail.com', password = 'kingkong@gmail.com', confirm_password = 'kingkong@gmail.com'), follow_redirects =True)
        self.assertTrue(b'That username is already taken!' in response.data)

    
    #register_SUCCESS
    def test_register(self):
        with current_app.app_context():
            tester = current_app.test_client(self)
            response = tester.post('/signup', data = dict(username='admin12',email = 'admin12@gmail.com', password = 'admin12@gmail.com', confirm_password = 'admin12@gmail.com'), follow_redirects =True)
            email = request.form.get('username')
            print(email)
        #self.assertNotIn('admin12',db())

""" #signin_FAIL
    def test_login(self):
        tester = current_app.test_client(self)
        tester.post('/signin', data = dict(email = 'kingkocng@gmail.com', password = 'kingkocng@gmail.com'),follow_redirects =True)
        response = tester.get( '/signin', follow_redirects = True)
        self.assertTrue(b'This website was built admist the Pandemic :)' in response.data)   """

"""     #signin_SUCCESS
    def test_login(self):
        tester = current_app.test_client(self)
        response = tester.post('/signin', data = dict(email = 'kingkong@gmail.com', password = 'kingkong@gmail.com'), follow_redirects =True) """
       # self.assertIn(b'kingkongpost', response.data)
    
 
        #self.assertIn(b'Log In', response.data) """


if __name__ == '__main__':
    unittest.main()