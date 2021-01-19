from flaskapp import app
import unittest

class FlaskTest(unittest.TestCase):
    #TEST_ROUTES
    #home
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/home', content_type='html')
        self.assertFalse(b'New Post' in response.data)
        
    #about
    def test_about(self):
        tester = app.test_client(self)
        response = tester.get('/about', content_type='html')        
        self.assertTrue(b'This is about page.' in response.data)

    #signin_FAIL
    def test_login(self):
        tester = app.test_client(self)
        tester.post('/signin', data = dict(email = 'kingkocng@gmail.com', password = 'kingkocng@gmail.com'),follow_redirects =True)
        response = tester.get( '/signin', follow_redirects = True)
        self.assertIn(b'login unsuccessful :)' , response.data)

"""     #signin_SUCCESS
    def test_login(self):
        tester = app.test_client(self)
        response = tester.post('/signin', data = dict(email = 'kingkong@gmail.com', password = 'kingkong@gmail.com'), follow_redirects =True) """
       # self.assertIn(b'kingkongpost', response.data)
    
    #register_FAILED
"""     def test_register(self):
        tester = app.test_client(self)
        response = tester.post('/signup', data = dict(username='admin5', email = 'adminsasas@gmail.com', password = 'admin0075', confirm_password = 'admin0075'), follow_redirects =True)
        response = tester.get(/signup)
        #self.assertTrue(b'That username is already taken!' in response.data)
        
        #self.assertIn(b'Log In', response.data) """
    
"""     #register_SUCCESS
    def test_register(self):
        tester = app.test_client(self)
        response = tester.post('/signup', data = dict(username='admin6',email = 'admin6@gmail.com', password = 'admin00756', confirm_password = 'admin00756'), follow_redirects =True)
        self.assertTrue(b'That username is already taken!' in response.data)

        
        #self.assertTrue(b'Your account has been created, you can now login!' in response.data) 
 """


"""     #Failed_signin  
 """

if __name__ == '__main__':
    unittest.main()