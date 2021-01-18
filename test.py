from flaskapp import app
import unittest

class FlaskTest(unittest.TestCase):
    #TEST_ROUTES
    #home
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/home', content_type='html')
        self.assertEqual(response.status_code, 200)
    
    #about
    def test_about(self):
        tester = app.test_client(self)
        response = tester.get('/about', content_type='html')
        self.assertEqual(response.status_code, 200)
    
    #signup
    def test_signup(self):
        tester = app.test_client(self)
        response = tester.get('/signup', content_type='html')
        self.assertEqual(response.status_code, 200)

    #signin
    def test_signin(self):
        tester = app.test_client(self)
        response = tester.get('/signin', content_type='html')
        self.assertEqual(response.status_code, 200)

    #logout
    def test_logout(self):
        tester = app.test_client(self)
        response = tester.get('/logout', content_type='html')
        self.assertEqual(response.status_code, 200)
    
    


if __name__ == '__main__':
    unittest.main()