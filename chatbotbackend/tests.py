import json
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework_simplejwt.tokens import Token
from rest_framework.test import APITestCase
from rest_framework import status
from accounts.models import UserAccount
from accounts.serializers import UserCreateSerializer
import pdb

class TestSetup(APITestCase):
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

        return super().setUp()

    def tearDown(self):
        return super().tearDown()
    
class AccountRegisterTestCase(APITestCase):
    def setUp(self):
        self.register_data = {  "first_name" : "testuser", 
                                "last_name" : "test",
                                "email" : "test@gmail.com",
                                "password" : "strongPassword123",
                                "re_password": "strongPassword123" }
        self.register_url = "/auth/users/"
        return super().setUp()

    def test_registration(self):
        response = self.client.post(self.register_url, self.register_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_registration_password_mismatch(self):
        self.register_data['re_password'] = "strong"
        response = self.client.post("/auth/users/", self.register_data)
        #pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['non_field_errors'][0], "The two password fields didn't match.")

class AccountLoginTestCase(APITestCase):
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
        self.response = self.client.post(self.register_url, self.register_data)
        return super().setUp()

    def activate_user(self):
        email = self.response.data['email']
        user = UserAccount.objects.get(email=email)
        user.is_active = True
        user.save()

    def test_login_not_activated(self):
        response = self.client.post(self.login_url, self.login_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'], "No active account found with the given credentials")
    
    def test_login_activated(self):
        self.activate_user()
        response = self.client.post(self.login_url, self.login_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class AccountDetailsTestCase(APITestCase):   
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
        self.user_details_url = "/auth/users/me/"
        self.register_response = self.client.post(self.register_url, self.register_data)
        self.activate_user()
        self.login_response = self.client.post(self.login_url, self.login_data)
        self.authentication()
        return super().setUp()
    
    def authentication(self):
        self.access_code = self.login_response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION="JWT "+ self.access_code)

    def activate_user(self):
        email = self.register_response.data['email']
        user = UserAccount.objects.get(email=email)
        user.is_active = True
        user.save()

    def test_get_current_user_details(self):
        response = self.client.get(self.user_details_url)
        #pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        