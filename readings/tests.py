import uuid
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from .factories import UserFactory, ReadingFactory

# Create your tests here.
class GlucoseLevelsTestCase(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.level = ReadingFactory()
        self.client.force_authenticate(self.user)
        
    def test_list_levels(self):
        response = self.client.get('/api/v1/levels/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['results'][0]['device'], "FreeStyle LibreLink")
        
    def test_list_levels_can_be_filtered_by_user_id(self):
        response = self.client.get(f'/api/v1/levels/?user_id={self.user.user_id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['results'][0]['serial_number'], "e09bb0f0-018b-429b-94c7-62bb306a0564")
        
    def test_retrieve_levels(self):
        level = ReadingFactory(user=self.user, device = "FreeStyle LibreLink",
                                    serial_number = "e09cc0f0-018b-429b-94c7-62bb306a0123",
                                    device_timestamp = "2022-02-08T09:08:00Z",
                                    recording_type = "0",
                                    glucose_value_history = "250")
        response = self.client.get(f'/api/v1/levels/{level.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['serial_number'], "e09cc0f0-018b-429b-94c7-62bb306a0123")
        
    def test_create_levels(self):
        data = {
            "device": "FreeStyle LibreLink",
            "serial_number": "e09bb0f0-018b-429b-94c7-62bb306a0564",
            "device_timestamp": "2022-02-08T09:08:00Z",
            "recording_type": "0",
            "glucose_value_history": "138",
        }
        response = self.client.post('/api/v1/levels/', data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['serial_number'], "e09bb0f0-018b-429b-94c7-62bb306a0564")
    