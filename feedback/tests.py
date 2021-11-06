from rest_framework.test import APITestCase
from rest_framework import status
from accounts.models import UserAccount
import pdb

class FeedbackTestCase(APITestCase):
    def setUp(self):
        self.register_data = {  "first_name" : "testuser", 
                                "last_name" : "test",
                                "email" : "test@gmail.com",
                                "password" : "strongPassword123",
                                "re_password": "strongPassword123" }
        self.login_data = { "email" : "test@gmail.com",
                            "password" : "strongPassword123"} 
        self.feedback_data = {  "user_id" : "1", 
                                "rating" : "3",
                                "feedback" : "test feedback description",
                                "domain" : "telecom",
                                "chatsession": {"sender": "testUser", "message" : "test message"} }
        self.feedback_url = "/feedback/"
        self.register_url = "/auth/users/"
        self.login_url = "/auth/jwt/create/"

        self.user_register()
        self.user_login()

        return super().setUp()

    def user_register(self):
        response = self.client.post(self.register_url, self.register_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.feedback_data['user_id'] = response.data['id']
        email = response.data['email']
        user = UserAccount.objects.get(email=email)
        user.is_active = True
        user.save()
    
    def user_login(self):
        response = self.client.post(self.login_url, self.login_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_record_feedback(self):
        response = self.client.post(self.feedback_url, self.feedback_data, format='json')
        #pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_get_feedback_data(self):
        self.client.post(self.feedback_url, self.feedback_data, format='json')
        response = self.client.get(self.feedback_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        