# To execute this test run python test.py on the Terminal
from portfolio.application.base import application
from portfolio.models import needs_db
import os
import json
import unittest
import tempfile

class PortfolioTestCase(unittest.TestCase):
    def setUp(self):
        self.tester = application.test_client()
    
    def login(self):
        passwd = "somepassword"
        self.tester.post('/admin/api/login', 
                       data=json.dumps(dict(password=passwd)),
                       content_type='application/json')

    def test_login(self):
        passwd = "somepassword"
        response = self.tester.post('/admin/api/login', 
                       data=json.dumps(dict(password=passwd)),
                       content_type='application/json')
        self.assertEqual(json.loads(response.data.decode('utf-8')), {'auth':True})
        passwd = "notsomepassword"
        response = self.tester.post('/admin/api/login', 
                       data=json.dumps(dict(password=passwd)),
                       content_type='application/json')
        self.assertEqual(json.loads(response.data.decode('utf-8')), {'auth':False})
    
    def test_logged_in(self):
        response = self.tester.get('/admin/api/logged_in')
        self.assertEqual(json.loads(response.data.decode('utf-8')), {'auth':False})
        self.login()
        response = self.tester.get('/admin/api/logged_in')
        self.assertEqual(json.loads(response.data.decode('utf-8')), {'auth':True})
       

    def test_logout(self):
        response = self.tester.get('/admin/api/logout')
        self.assertEqual(json.loads(response.data.decode('utf-8')), {'error':"Not logged in"})
        self.login()
        response = self.tester.get('/admin/api/logout')
        self.assertEqual(response.status_code, 204)
        response = self.tester.get('/admin/api/logout')
        self.assertEqual(json.loads(response.data.decode('utf-8')), {'error':"Not logged in"})
    
    def test_home_status_code(self):
        response = self.tester.get('/')
        self.assertEqual(response.status_code, 200)

    def test_count(self):
        response = self.tester.get('/api/projects/count', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data.decode('utf-8')), {'count':0})

    def test_project_new(self):
        self.login()
        response = self.tester.post('/admin/api/projects/new', 
                       data=json.dumps(dict(name='foo', url="http://", show=True, description="bar")),
                       content_type='application/json')
        self.assertEqual(response.status_code, 204)

        #adding two projects - ideally would like this to have this preset in test database
        response = self.tester.post('/admin/api/projects/new', 
                       data=json.dumps(dict(name='foo', url="http://", show=True, description="bar")),
                       content_type='application/json')
        self.assertEqual(response.status_code, 204)
    
    def test_project_read(self):
        response = self.tester.get('/api/projects/1', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data.decode('utf-8')), {'key':1, 'name':'foo','url':"http://", 'show':True, 'description':"bar" })
    
    def test_project_write(self):
        self.login()
        #test valid update
        response = self.tester.post('/admin/api/projects/2', 
                       data=json.dumps(dict(name='foop', description='barp', show = False, url="https://")),
                       content_type='application/json')
        self.assertEqual(response.status_code, 204)
        response = self.tester.get('/api/projects/2', content_type='application/json')
        self.assertEqual(response.status_code, 200)

        #test invalid update
        self.assertEqual(json.loads(response.data.decode('utf-8')), {'key':2, 'name':'foop','url':"https://", 'show':False, 'description':"barp" })
        response = self.tester.post('/admin/api/projects/2', 
                       data=json.dumps(None),
                       content_type='application/json')
        self.assertEqual(response.status_code, 400)
        

if __name__ == '__main__':
    unittest.main()
