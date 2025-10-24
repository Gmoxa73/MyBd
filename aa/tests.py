from django.test import TestCase
from rest_framework.test import APIClient


class MyTest(TestCase):
    def test_ok(self):
        self.assertTrue(True)

    def test_sample_view(self):
        url = "/list/"
        client = APIClient()
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
