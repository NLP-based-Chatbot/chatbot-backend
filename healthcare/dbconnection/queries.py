from django.shortcuts import render
import requests
from django.http import JsonResponse,HttpResponse
from django.core import serializers
import json
import datetime

import random
import string

from healthcare.models import *

def speclist(data):
    return Specialization.objects.all()

def doctlist(data):
    try:
        spec_id = data["spec_id"]
    except KeyError:
        spec_id = None

    if spec_id == None or spec_id=="":
        return Doctor.objects.all()
    
    doc2spec =  DoctorSpec.objects.filter(spec_id=spec_id)

    result=[]

    for doc in doc2spec:
        result.append(Doctor.objects.filter(doctor_id=doc.doctor_id_id)[0])

    return result
        
    

def newappoint(data):
    doct_id = data["doct_id"]
    cust_id = data["cust_id"]
    date = data["date"]
    time = data["time"]

    try:
        doc = Doctor.objects.get(doctor_id=doct_id)
        cust = Patient.objects.get(cust_id=cust_id)
        new_appointment = Appiontment(doctor_id_id=doc.doctor_id, cust_id_id=cust.cust_id,date=date,time_slot=time)
        new_appointment.save()
        return '[{"query_success":"1"}]'
    except Exception as e:
        return '[{"query_success":"0","error":\"'+str(e)+'\"}]'



def changeappoint(data):
    cust_id = data["cust_id"]
    appoint_id = data["appoint_id"]
    date = data["date"]
    time = data["time"]

    try:
        alt_appointment = Appiontment.objects.get(appointment_id=appoint_id,cust_id=cust_id)
    except Exception as e:
        return '[{"query_success":"0","error":\"'+str(e)+'\"}]'

    alt_appointment.date=date
    alt_appointment.time_slot=time

    try:
        alt_appointment.save()
        return '[{"query_success":"1"}]'
    except Exception as e:
        return '[{"query_success":"0","error":\"'+str(e)+'\"}]'

def deleteappoint(data):
    cust_id = data["cust_id"]
    appoint_id = data["appoint_id"]

    try:
        del_appointment = Appiontment.objects.get(appointment_id=appoint_id,cust_id=cust_id)
    except Exception as e:
        return '[{"query_success":"0","error":\"'+str(e)+'\"}]'

    if del_appointment==None:
        return '[{"query_success":"0","error":"No appointment was found with above detailes"}]'

    try:
        del_appointment.delete()
        return '[{"query_success":"1"}]'
    except Exception as e:
        return '[{"query_success":"0","error":\"'+str(e)+'\"}]'

def listappoint(data):
    cust_id = data["cust_id"]
    try:
        customer = Patient.objects.get(cust_id=cust_id)
        return Appiontment.objects.filter(cust_id=customer.cust_id,date__gte=datetime.date.today())
    except Exception:
        return '[]'

def docbyhash(data):
    docthash = data["docthash"]
    return Doctor.objects.filter(docthash=docthash)

def docavlbl(data):
    docthash = data["docthash"]

    try:
        doct_id = Doctor.objects.get(docthash=docthash).doctor_id
        return DoctorAvailable.objects.filter(doctor_id=doct_id)
    except Exception:
        return '[]'
    
def clientdata(data):
    userhash = data["userhash"]
    return Patient.objects.filter(userhash=userhash)

def newpatient(data):
    username = data["username"]
    userhash = "usr_"+''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(25))

    try:
        new_patient = Patient(username=username,userhash=userhash)
        new_patient.save()
        return Patient.objects.filter(userhash=userhash)
    except Exception as e:
        return '[{"query_success":"0","error":\"'+str(e)+'\"}]'

def newreport(data):
    cust_id = data["cust_id"]
    report_name = data["report_name"]
    available_on = data["available_on"]

    try:
        assert report_name!="" and report_name!=None
        reporthash = "report_"+''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(25))
        customer = Patient.objects.get(cust_id=cust_id)
        new_report = Report(cust_id=customer,report_name=report_name,reporthash=reporthash,available_on=available_on)
        new_report.save()
        return Report.objects.filter(reporthash=reporthash)
    except Exception as e:
        return '[{"query_success":"0","error":\"'+str(e)+'\"}]'

def listreports(data):
    cust_id = data["cust_id"]
    customer = Patient.objects.get(cust_id=cust_id)
    return Report.objects.filter(cust_id=customer.cust_id)

def getreport(data):
    cust_id = data["cust_id"]
    reporthash = data["reporthash"]
    customer = Patient.objects.filter(cust_id=cust_id)
    return Report.objects.filter(cust_id=customer[0].cust_id,reporthash=reporthash)

def placemedtest(data):
    cust_id = data["cust_id"]
    date = data["date"]
    time = data["time"]
    test_type = data["test_type"]
    report_id = data["report_id"]
    
    try:
        assert test_type!=None and test_type!=""

        cust = Patient.objects.get(cust_id=cust_id)
        report = Report.objects.get(report_id=report_id)

        medtest = MedicalTest(
            cust_id_id=cust.cust_id,
            date=date,
            time_slot= time,
            test_type=test_type,
            report_id=report
        )
        medtest.save()
        return '[{"query_success":"1"}]'
    except Exception as e:
        return '[{"query_success":"0","error":\"'+str(e)+'\"}]'

def listmedtest(data):
    cust_id = data["cust_id"]
    customer = Patient.objects.filter(cust_id=cust_id)
    return MedicalTest.objects.filter(cust_id=customer[0].cust_id,date__gte=datetime.date.today())

def makecomplain(data):
    title = data["title"]
    description = data["description"]
    name = data["name"]
    contact_no = data["contact_no"]
    email = data["email"]
    
    try:
        assert title!=None and title!=""
        assert description!=None and description!=""
        assert name!=None and name!=""
        assert contact_no!=None and contact_no!=""
        assert email!=None and email!=""

        complaint = Complaint(
            title=title,
            description=description,
            name=name,
            contact_no=contact_no,
            email=email
        )
        complaint.save()
        return '[{"query_success":"1"}]'
    except Exception as e:
        return '[{"query_success":"0","error":\"'+str(e)+'\"}]'

map2func = {
    "speclist": speclist,
    "doctlist": doctlist,
    "newappoint": newappoint,
    "changeappoint": changeappoint,
    "deleteappoint": deleteappoint,
    "listappoint": listappoint,
    "docbyhash": docbyhash,
    "docavlbl": docavlbl,
    "clientdata": clientdata,
    "newpatient": newpatient,
    "listreports": listreports,
    "getreport":getreport,
    "makecomplain":makecomplain,
    "placemedtest":placemedtest,
    "listmedtest":listmedtest,
    "newreport":newreport,
}

def runquery(request):
    querydata=request.body
    querydata_dict = json.loads(querydata)

    func_to_exc = querydata_dict["function"]

    result = map2func[func_to_exc](querydata_dict["data"])

    try:
        result_json = serializers.serialize('json', result)
    except Exception:
        result_json = result

    return HttpResponse(result_json, content_type='application/json')
