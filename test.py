from flaskapp import app
import unittest

class FlaskTest(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/home', content_type='html')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()