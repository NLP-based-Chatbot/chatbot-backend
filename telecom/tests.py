from rest_framework.test import APITestCase
from rest_framework import status
from accounts.models import UserAccount
import pdb

class TelecomTestCase(APITestCase):
    def setUp(self):
        self.service_provider = "dialog"
        self.payment_method = "postpaid"
        self.package_type = "unlimited"

        self.url = "/packages/"+self.service_provider+"/"+self.payment_method+"/"+self.package_type 
        return super().setUp()


    def test_get_package_details(self):
        response = self.client.get(self.url)
        #pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
        