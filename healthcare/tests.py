from django.test import TestCase

from rest_framework.test import APITestCase
from rest_framework import status
from healthcare.models import *
from accounts.models import UserAccount
import pdb

class HealthcareDBQueryTest(APITestCase):
    def setUp(self):
        self.register_data = {  "first_name" : "testuser", 
                                "last_name" : "test",
                                "email" : "test@gmail.com",
                                "password" : "strongPassword123",
                                "re_password": "strongPassword123" }
        self.login_data = { "email" : "test@gmail.com",
                            "password" : "strongPassword123"} 
        
        self.register_url = "/auth/users/"
        self.login_url = "/auth/jwt/create/"

        self.query_url = "/healthcare/query/"

        self.user_register()
        self.user_login()
        self.authentication()
        
        return super().setUp()
    
    def authentication(self):
        self.access_code = self.login_response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION="JWT "+ self.access_code)

    def user_register(self):
        response = self.client.post(self.register_url, self.register_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user_id = response.data['id']
        email = response.data['email']
        user = UserAccount.objects.get(email=email)
        user.is_active = True
        user.save()
    
    def user_login(self):
        self.login_response = self.client.post(self.login_url, self.login_data)
        self.assertEqual(self.login_response.status_code, status.HTTP_200_OK)

        
    def test_get_speclist(self):
        data = {
            "function":"speclist",
            "data":{}
        }
        response = self.client.post(self.query_url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_doc_with_spec(self):
        data = {
            "function":"doctlist",
            "data":{
                "spec_id":"1"
            }
        }
        response = self.client.post(self.query_url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_doc_no_spec(self):
        data = {
            "function":"doctlist",
            "data":{}
        }
        response = self.client.post(self.query_url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_place_appointment(self):
        data = {
            "function":"newappoint",
            "data":{
                "doct_id":"1",
                "cust_id":"51",
                "date":"2029-10-05",
                "time":"20:00"
            }
        }
        response = self.client.post(self.query_url,data,format='json')
        
        self.assertEqual(response.content,b'[{"query_success":"1"}]')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_change_appointment(self):
        data = {
            "function":"changeappoint",
            "data":{
                "appoint_id":"1",
                "cust_id":"2",
                "date":"2025-10-05",
                "time":"21:00"
            }
        }
        response = self.client.post(self.query_url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_appointment(self):
        data = {
            "function":"deleteappoint",
            "data":{
                "appoint_id":"5",
                "cust_id":"4"
            }
        }
        response = self.client.post(self.query_url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_appointment(self):
        data = {
            "function":"listappoint",
            "data":{
                "cust_id":"5"
            }
        }
        response = self.client.post(self.query_url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_doct_available(self):
        data = {
            "function":"docavlbl",
            "data":{
                "docthash":"doc_cd6sg9fgsfd5g5f8sgfg5sg95"
            }
        }
        response = self.client.post(self.query_url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)