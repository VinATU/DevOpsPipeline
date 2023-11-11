import unittest
from flask import Flask, url_for
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello, World to DevOps Project!')

    def test_hello_route_get(self):
        response = self.app.get('/hello')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Enter your name:', response.data)

    def test_hello_route_post(self):
        response = self.app.post('/hello', data={'name': 'John'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, John!', response.data)

if __name__ == '__main__':
    unittest.main()
