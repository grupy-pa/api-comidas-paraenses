from django.test import TestCase

from rest_framework.test import APIClient

client = APIClient()

class StatusViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_status(self):
        response = self.client.get('/api/v1/comidas-paraenses/status/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"message": "API funcionando!"})
      
# Create your tests here.
