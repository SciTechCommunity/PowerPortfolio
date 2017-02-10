# To execute this test run python test.py on the Terminal
from portfolio.application.base import application
from portfolio.models import needs_db
import os
import json
import unittest
import tempfile

class PortfolioTestCase(unittest.TestCase):
    def setUp(self):
        self.application = application.test_client()

    def test_home_status_code(self):
        result = self.application.get('/')
        self.assertEqual(result.status_code, 200)

    def test_count(self):
        tester = application.test_client(self)
        response = tester.get('/api/projects/count', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data.decode('utf-8')), {'count':0})

    def test_project_new(self):
        tester = application.test_client(self)
        response = tester.post('/admin/api/projects/new', 
                       data=json.dumps(dict(name='foo', url="http://", show=True, description="bar")),
                       content_type='application/json')
        self.assertEqual(response.status_code, 204)

        #adding two projects - ideally would like this to have this preset in test database
        response = tester.post('/admin/api/projects/new', 
                       data=json.dumps(dict(name='foo', url="http://", show=True, description="bar")),
                       content_type='application/json')
        self.assertEqual(response.status_code, 204)
    
    def test_project_read(self):
        tester = application.test_client(self)
        response = tester.get('/api/projects/1', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data.decode('utf-8')), {'key':1, 'name':'foo','url':"http://", 'show':True, 'description':"bar" })
    
    def test_project_write(self):
        tester = application.test_client(self)
        
        #test valid update
        response = tester.post('/admin/api/projects/2', 
                       data=json.dumps(dict(name='foop', description='barp', show = False, url="https://")),
                       content_type='application/json')
        self.assertEqual(response.status_code, 204)
        response = tester.get('/api/projects/2', content_type='application/json')
        self.assertEqual(response.status_code, 200)

        #test invalid update
        self.assertEqual(json.loads(response.data.decode('utf-8')), {'key':2, 'name':'foop','url':"https://", 'show':False, 'description':"barp" })
        response = tester.post('/admin/api/projects/2', 
                       data=json.dumps(None),
                       content_type='application/json')
        self.assertEqual(response.status_code, 400)
       


        

if __name__ == '__main__':
    unittest.main()
