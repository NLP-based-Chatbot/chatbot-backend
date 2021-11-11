from django.test import TestCase

from rest_framework.test import APITestCase
from rest_framework import status
from healthcare.models import *
from accounts.models import UserAccount
import pdb
import json
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

########################################################################################

class  GeneralQueryTest(HealthcareDBQueryTest):
    def setUp(self):
        return super().setUp()

    def test_get_speclist(self):
        data = {
            "function":"speclist",
            "data":{}
        }
        response = self.client.post(self.query_url,data,format='json')
        res_dict = json.loads(response.content.decode())

        self.assertNotEqual(res_dict,[])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_doc_with_spec_exist(self):
        data = {
            "function":"doctlist",
            "data":{
                "spec_id":"1"
            }
        }
        response = self.client.post(self.query_url,data,format='json')
        res_dict = json.loads(response.content.decode())

        self.assertNotEqual(res_dict,[])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_doc_with_spec_doesnt_exist(self):
        data = {
            "function":"doctlist",
            "data":{
                "spec_id":"20"
            }
        }
        response = self.client.post(self.query_url,data,format='json')
        res_dict = json.loads(response.content.decode())

        self.assertEqual(res_dict,[])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_doc_no_spec(self):
        data = {
            "function":"doctlist",
            "data":{}
        }
        response = self.client.post(self.query_url,data,format='json')
        res_dict = json.loads(response.content.decode())

        self.assertNotEqual(res_dict,[])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_doct_available_doctor_exist(self):
        data = {
            "function":"docavlbl",
            "data":{
                "docthash":"doc_cd6sg9fgsfd5g5f8sgfg5sg95"
            }
        }
        response = self.client.post(self.query_url,data,format='json')
        res_dict = json.loads(response.content.decode())

        self.assertNotEqual(res_dict,[])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_doct_available_doctor_doesnt_exist(self):
        data = {
            "function":"docavlbl",
            "data":{
                "docthash":"doc_2hj5g4hg5k2h452k45g255k2"
            }
        }
        response = self.client.post(self.query_url,data,format='json')
        res_dict = json.loads(response.content.decode())

        self.assertEqual(res_dict,[])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

########################################################################################

class AppointmentQueryTest(HealthcareDBQueryTest):
    def setUp(self):
        return super().setUp()

    def test_place_appointment_all_ok(self):
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
        res_dict = json.loads(response.content.decode())

        self.assertEqual(res_dict[0]["query_success"],"1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_place_appointment_user_doesnt_exists(self):
        data = {
            "function":"newappoint",
            "data":{
                "doct_id":"1",
                "cust_id":"1",
                "date":"2029-10-05",
                "time":"20:00"
            }
        }
        response = self.client.post(self.query_url,data,format='json')
        res_dict = json.loads(response.content.decode())

        self.assertEqual(res_dict[0]["query_success"],"0")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_place_appointment_doctor_doesnt_exists(self):
        data = {
            "function":"newappoint",
            "data":{
                "doct_id":"20",
                "cust_id":"51",
                "date":"2029-10-05",
                "time":"20:00"
            }
        }
        response = self.client.post(self.query_url,data,format='json')
        res_dict = json.loads(response.content.decode())

        self.assertEqual(res_dict[0]["query_success"],"0")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_change_appointment_all_ok(self):
        data = {
            "function":"changeappoint",
            "data":{
                "appoint_id":"26",
                "cust_id":"51",
                "date":"2025-10-05",
                "time":"21:00"
            }
        }
        response = self.client.post(self.query_url,data,format='json')
        res_dict = json.loads(response.content.decode())

        self.assertEqual(res_dict[0]["query_success"],"1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_change_appointment_user_doesnt_exit(self):
        data = {
            "function":"changeappoint",
            "data":{
                "appoint_id":"26",
                "cust_id":"1",
                "date":"2025-10-05",
                "time":"21:00"
            }
        }
        response = self.client.post(self.query_url,data,format='json')
        res_dict = json.loads(response.content.decode())

        self.assertEqual(res_dict[0]["query_success"],"0")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_change_appointment_appoint_doesnt_exist(self):
        data = {
            "function":"changeappoint",
            "data":{
                "appoint_id":"6",
                "cust_id":"51",
                "date":"2025-10-05",
                "time":"21:00"
            }
        }
        response = self.client.post(self.query_url,data,format='json')
        res_dict = json.loads(response.content.decode())

        self.assertEqual(res_dict[0]["query_success"],"0")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_appointment_all_ok(self):
        data = {
            "function":"deleteappoint",
            "data":{
                "appoint_id":"26",
                "cust_id":"51"
            }
        }
        response = self.client.post(self.query_url,data,format='json')
        res_dict = json.loads(response.content.decode())

        self.assertEqual(res_dict[0]["query_success"],"1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_appointment_user_doesnt_exist(self):
        data = {
            "function":"deleteappoint",
            "data":{
                "appoint_id":"26",
                "cust_id":"1"
            }
        }
        response = self.client.post(self.query_url,data,format='json')
        res_dict = json.loads(response.content.decode())

        self.assertEqual(res_dict[0]["query_success"],"0")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_appointment_appoint_doesnt_exist(self):
        data = {
            "function":"deleteappoint",
            "data":{
                "appoint_id":"1",
                "cust_id":"51"
            }
        }
        response = self.client.post(self.query_url,data,format='json')
        res_dict = json.loads(response.content.decode())

        self.assertEqual(res_dict[0]["query_success"],"0")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_appointment_user_has_appointments(self):
        data = {
            "function":"listappoint",
            "data":{
                "cust_id":"51"
            }
        }
        response = self.client.post(self.query_url,data,format='json')
        res_dict = json.loads(response.content.decode())

        self.assertNotEqual(res_dict,[])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_appointment_user_has_no_appointments(self):
        data = {
            "function":"listappoint",
            "data":{
                "cust_id":"50"
            }
        }
        response = self.client.post(self.query_url,data,format='json')
        res_dict = json.loads(response.content.decode())

        self.assertEqual(res_dict,[])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_appointment_user_doesnt_exist(self):
        data = {
            "function":"listappoint",
            "data":{
                "cust_id":"1"
            }
        }
        response = self.client.post(self.query_url,data,format='json')
        res_dict = json.loads(response.content.decode())

        self.assertEqual(res_dict,[])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

########################################################################################

class ReportsQueryTest(HealthcareDBQueryTest):
    def setUp(self):
        return super().setUp()

    def test_new_reports_all_ok(self):
        data = {
            "function":"newreport",
            "data":{
                "cust_id":"51",
                "report_name":"test_teport",
                "available_on":"2022-01-01"
            }
        }
        response = self.client.post(self.query_url,data,format='json')
        res_dict = json.loads(response.content.decode())

        assert( "query_success" not in res_dict[0].keys())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_new_reports_user_doesnt_exist(self):
        data = {
            "function":"newreport",
            "data":{
                "cust_id":"1",
                "report_name":"test_teport",
                "available_on":"2022-01-01"
            }
        }
        response = self.client.post(self.query_url,data,format='json')
        res_dict = json.loads(response.content.decode())

        assert( "query_success" in res_dict[0].keys())
        self.assertEqual(res_dict[0]["query_success"],"0")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_new_reports_user_id_empty(self):
        data = {
            "function":"newreport",
            "data":{
                "cust_id":"",
                "report_name":"test_teport",
                "available_on":"2022-01-01"
            }
        }
        response = self.client.post(self.query_url,data,format='json')
        res_dict = json.loads(response.content.decode())

        assert( "query_success" in res_dict[0].keys())
        self.assertEqual(res_dict[0]["query_success"],"0")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_new_reports_no_report_name(self):
        data = {
            "function":"newreport",
            "data":{
                "cust_id":"51",
                "report_name":"",
                "available_on":"2022-01-01"
            }
        }
        response = self.client.post(self.query_url,data,format='json')
        res_dict = json.loads(response.content.decode())

        assert( "query_success" in res_dict[0].keys())
        self.assertEqual(res_dict[0]["query_success"],"0")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_new_reports_not_a_date(self):
        data = {
            "function":"newreport",
            "data":{
                "cust_id":"51",
                "report_name":"test_teport",
                "available_on":"2j42jk34j32"
            }
        }
        response = self.client.post(self.query_url,data,format='json')
        res_dict = json.loads(response.content.decode())

        assert( "query_success" in res_dict[0].keys())
        self.assertEqual(res_dict[0]["query_success"],"0")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_reports_user_exist(self):
        data = {
            "function":"listreports",
            "data":{
                "cust_id":"51"
            }
        }
        response = self.client.post(self.query_url,data,format='json')
        res_dict = json.loads(response.content.decode())

        self.assertNotEqual(res_dict,[])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_reports_user_doesnt_exist(self):
        data = {
            "function":"listreports",
            "data":{
                "cust_id":"51"
            }
        }
        response = self.client.post(self.query_url,data,format='json')
        res_dict = json.loads(response.content.decode())

        self.assertNotEqual(res_dict,[])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

########################################################################################

class MedicalTestQueryTest(HealthcareDBQueryTest):
    def setUp(self):
        return super().setUp()

    def test_place_medtest_all_ok(self):
        report_data = {
            "function":"newreport",
            "data":{
                "cust_id":"51",
                "report_name":"test_teport",
                "available_on":"2022-01-01"
            }
        }

        response = self.client.post(self.query_url,report_data,format='json')
        res_dict = json.loads(response.content.decode())

        report_id = res_dict[0]["pk"]

        data = {
            "function":"placemedtest",
            "data":{
                "cust_id":"51",
                "date":"2022-01-01",
                "time":"20:00",
                "test_type":"ecg",
                "report_id":report_id
            }
        }
        response = self.client.post(self.query_url,data,format='json')
        res_dict = json.loads(response.content.decode())

        assert( "query_success" in res_dict[0].keys())
        self.assertEqual(res_dict[0]["query_success"],"1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_place_medtest_user_doesnt_exist(self):
        report_data = {
            "function":"newreport",
            "data":{
                "cust_id":"51",
                "report_name":"test_teport",
                "available_on":"2022-01-01"
            }
        }

        response = self.client.post(self.query_url,report_data,format='json')
        res_dict = json.loads(response.content.decode())

        report_id = res_dict[0]["pk"]

        data = {
            "function":"placemedtest",
            "data":{
                "cust_id":"1",
                "date":"2022-01-01",
                "time":"20:00",
                "test_type":"ecg",
                "report_id":report_id
            }
        }
        response = self.client.post(self.query_url,data,format='json')
        res_dict = json.loads(response.content.decode())

        assert( "query_success" in res_dict[0].keys())
        self.assertEqual(res_dict[0]["query_success"],"0")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_place_medtest_not_a_date(self):
        report_data = {
            "function":"newreport",
            "data":{
                "cust_id":"51",
                "report_name":"test_teport",
                "available_on":"2022-01-01"
            }
        }

        response = self.client.post(self.query_url,report_data,format='json')
        res_dict = json.loads(response.content.decode())

        report_id = res_dict[0]["pk"]

        data = {
            "function":"placemedtest",
            "data":{
                "cust_id":"51",
                "date":"h423g43jkg543",
                "time":"20:00",
                "test_type":"ecg",
                "report_id":report_id
            }
        }
        response = self.client.post(self.query_url,data,format='json')
        res_dict = json.loads(response.content.decode())

        assert( "query_success" in res_dict[0].keys())
        self.assertEqual(res_dict[0]["query_success"],"0")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_place_medtest_not_a_time(self):
        report_data = {
            "function":"newreport",
            "data":{
                "cust_id":"51",
                "report_name":"test_teport",
                "available_on":"2022-01-01"
            }
        }

        response = self.client.post(self.query_url,report_data,format='json')
        res_dict = json.loads(response.content.decode())

        report_id = res_dict[0]["pk"]

        data = {
            "function":"placemedtest",
            "data":{
                "cust_id":"51",
                "date":"2022-01-01",
                "time":"4234kj3h24k2",
                "test_type":"ecg",
                "report_id":report_id
            }
        }
        response = self.client.post(self.query_url,data,format='json')
        res_dict = json.loads(response.content.decode())

        assert( "query_success" in res_dict[0].keys())
        self.assertEqual(res_dict[0]["query_success"],"0")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_place_medtest_test_type_not_provided(self):
        report_data = {
            "function":"newreport",
            "data":{
                "cust_id":"51",
                "report_name":"test_teport",
                "available_on":"2022-01-01"
            }
        }

        response = self.client.post(self.query_url,report_data,format='json')
        res_dict = json.loads(response.content.decode())

        report_id = res_dict[0]["pk"]

        data = {
            "function":"placemedtest",
            "data":{
                "cust_id":"51",
                "date":"2022-01-01",
                "time":"20:00",
                "test_type":"",
                "report_id":report_id
            }
        }
        response = self.client.post(self.query_url,data,format='json')
        res_dict = json.loads(response.content.decode())

        assert( "query_success" in res_dict[0].keys())
        self.assertEqual(res_dict[0]["query_success"],"0")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

########################################################################################

class ComplaintQueryTest(HealthcareDBQueryTest):
    def setUp(self):
        return super().setUp()

    def test_make_complain_all_ok(self):
        data = {
            "function":"makecomplain",
            "data":{
                "title":"Complain title",
                "description":"Complain description",
                "name":"Comlpainer's full name",
                "contact_no":"0112222222222",
                "email":"complainer@mail.com"
            }
        }

        response = self.client.post(self.query_url,data,format='json')
        res_dict = json.loads(response.content.decode())

        assert( "query_success" in res_dict[0].keys())
        self.assertEqual(res_dict[0]["query_success"],"1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_make_complain_no_title(self):
        data = {
            "function":"makecomplain",
            "data":{
                "title":"",
                "description":"Complain description",
                "name":"Comlpainer's full name",
                "contact_no":"0112222222222",
                "email":"complainer@mail.com"
            }
        }

        response = self.client.post(self.query_url,data,format='json')
        res_dict = json.loads(response.content.decode())

        assert( "query_success" in res_dict[0].keys())
        self.assertEqual(res_dict[0]["query_success"],"0")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_make_complain_no_description(self):
        data = {
            "function":"makecomplain",
            "data":{
                "title":"Complain title",
                "description":"",
                "name":"Comlpainer's full name",
                "contact_no":"0112222222222",
                "email":"complainer@mail.com"
            }
        }

        response = self.client.post(self.query_url,data,format='json')
        res_dict = json.loads(response.content.decode())

        assert( "query_success" in res_dict[0].keys())
        self.assertEqual(res_dict[0]["query_success"],"0")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_make_complain_no_name(self):
        data = {
            "function":"makecomplain",
            "data":{
                "title":"Complain title",
                "description":"Complain description",
                "name":"",
                "contact_no":"0112222222222",
                "email":"complainer@mail.com"
            }
        }

        response = self.client.post(self.query_url,data,format='json')
        res_dict = json.loads(response.content.decode())

        assert( "query_success" in res_dict[0].keys())
        self.assertEqual(res_dict[0]["query_success"],"0")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_make_complain_no_contact_no(self):
        data = {
            "function":"makecomplain",
            "data":{
                "title":"Complain title",
                "description":"Complain description",
                "name":"Comlpainer's full name",
                "contact_no":"",
                "email":"complainer@mail.com"
            }
        }

        response = self.client.post(self.query_url,data,format='json')
        res_dict = json.loads(response.content.decode())

        assert( "query_success" in res_dict[0].keys())
        self.assertEqual(res_dict[0]["query_success"],"0")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_make_complain_no_email(self):
        data = {
            "function":"makecomplain",
            "data":{
                "title":"Complain title",
                "description":"Complain description",
                "name":"Comlpainer's full name",
                "contact_no":"0112222222222",
                "email":""
            }
        }

        response = self.client.post(self.query_url,data,format='json')
        res_dict = json.loads(response.content.decode())

        assert( "query_success" in res_dict[0].keys())
        self.assertEqual(res_dict[0]["query_success"],"0")
        self.assertEqual(response.status_code, status.HTTP_200_OK)