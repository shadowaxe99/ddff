```python
import unittest
from flask import Flask
from backend.app import create_app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_app_creation(self):
        self.assertIsInstance(self.app, Flask)

    def test_home_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_dashboard_route(self):
        response = self.client.get('/dashboard')
        self.assertEqual(response.status_code, 200)

    def test_content_route(self):
        response = self.client.get('/content')
        self.assertEqual(response.status_code, 200)

    def test_writers_route(self):
        response = self.client.get('/writers')
        self.assertEqual(response.status_code, 200)

    def test_calendar_route(self):
        response = self.client.get('/calendar')
        self.assertEqual(response.status_code, 200)

    def test_analytics_route(self):
        response = self.client.get('/analytics')
        self.assertEqual(response.status_code, 200)

    def test_socialMedia_route(self):
        response = self.client.get('/socialMedia')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
```