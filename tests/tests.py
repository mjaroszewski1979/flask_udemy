import unittest
import re
import sys
import os



current = os.path.dirname(os.path.realpath(__file__))  
parent = os.path.dirname(current)  
sys.path.append(parent)

import run

app = run.create_app()


class RoutesTestCase(unittest.TestCase):

    # Ensures that the application instance exists
    def test_app_exists(self):
        self.assertIsNotNone(app)

    # Ensures that index page loads correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensures that the data returned contains actual text from the index page
    def test_index_data(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'Web Developer' in response.data)

    # Ensures that project01 page loads correctly
    def test_project01(self):
        tester = app.test_client(self)
        response = tester.get('/project01', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensures that the data returned contains actual text from the project01 page
    def test_project01_data(self):
        tester = app.test_client(self)
        response = tester.get('/project01', content_type='html/text')
        self.assertTrue(b'Project name: Lorem ipsum dolor sit amet.' in response.data)

    # Ensures that project02 page loads correctly
    def test_project02(self):
        tester = app.test_client(self)
        response = tester.get('/project02', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensures that the data returned contains actual text from the project02 page
    def test_project02_data(self):
        tester = app.test_client(self)
        response = tester.get('/project02', content_type='html/text')
        self.assertTrue(b'Company: Lorem ipsum dolor sit amet.' in response.data)

    # Ensures that project03 page loads correctly
    def test_project03(self):
        tester = app.test_client(self)
        response = tester.get('/project03', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensures that the data returned contains actual text from the project03 page
    def test_project03_data(self):
        tester = app.test_client(self)
        response = tester.get('/project03', content_type='html/text')
        self.assertTrue(b'Project description:' in response.data)

    # Ensures that project04 page loads correctly
    def test_project04(self):
        tester = app.test_client(self)
        response = tester.get('/project04', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensures that the data returned contains actual text from the project04 page
    def test_project04_data(self):
        tester = app.test_client(self)
        response = tester.get('/project04', content_type='html/text')
        self.assertTrue(b'Eos iure necessitatibus doloribus' in response.data)

    # Ensures that project05 page loads correctly
    def test_project05(self):
        tester = app.test_client(self)
        response = tester.get('/project05', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensures that the data returned contains actual text from the project05 page
    def test_project05_data(self):
        tester = app.test_client(self)
        response = tester.get('/project05', content_type='html/text')
        self.assertTrue(b'Exercitationem delectus nemo ipsa natus culpa earum' in response.data)

    # Ensures that the success page loads correctly given valid name and email
    def test_success_post(self):
        tester = app.test_client(self)
        response = tester.post('/success', 
        data=dict(name='r"[A-Z][a-z]+,?\s+(?:[A-Z][a-z]*\.?\s*)?[A-Z][a-z]+"', 
        email="r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'", message='r"[A-Z][a-z]+,?\s+(?:[A-Z][a-z]*\.?\s*)?[A-Z][a-z]+"'), follow_redirects=True)
        self.assertIn(b'I will contact you on', response.data)

    # Ensures that error/404 page loads correctly
    def test_404(self):
        tester = app.test_client(self)
        response = tester.get('/404', content_type='html/text')
        self.assertEqual(response.status_code, 404)

    # Ensures that the data returned contains actual text from the error/404 page
    def test_404_data(self):
        tester = app.test_client(self)
        response = tester.get('/404', content_type='html/text')
        self.assertTrue(b'error404.png' in response.data)


if __name__ == '__main__':
    unittest.main()