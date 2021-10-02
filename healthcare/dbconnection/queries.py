from django.shortcuts import render
import requests
from django.http import JsonResponse,HttpResponse
from django.core import serializers
import json
import datetime

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

    doc = Doctor.objects.get(doctor_id=doct_id)
    cust = Patient.objects.get(cust_id=cust_id)

    new_appointment = Appiontment(doctor_id_id=doc.doctor_id, cust_id_id=cust.cust_id,date=date,time_slot=time)

    try:
        new_appointment.save()
        return '[{"query_success":"1"}]'
    except Exception as e:
        return '[{"query_success":"0","error":'+str(e)+'}]'



def changeappoint(data):
    cust_id = data["cust_id"]
    appoint_id = data["appoint_id"]
    date = data["date"]
    time = data["time"]

    try:
        alt_appointment = Appiontment.objects.get(appointment_id=appoint_id,cust_id=cust_id)
    except Exception as e:
        return '[{"query_success":"0","error":'+str(e)+'}]'

    alt_appointment.date=date
    alt_appointment.time_slot=time

    try:
        alt_appointment.save()
        return '[{"query_success":"1"}]'
    except Exception as e:
        return '[{"query_success":"0","error":'+str(e)+'}]'

def deleteappoint(data):
    cust_id = data["cust_id"]
    appoint_id = data["appoint_id"]

    try:
        del_appointment = Appiontment.objects.get(appointment_id=appoint_id,cust_id=cust_id)
    except Exception as e:
        return '[{"query_success":"0","error":'+str(e)+'}]'

    if del_appointment==None:
        return '[{"query_success":"0","error":"No appointment was found with above detailes"}]'

    try:
        del_appointment.delete()
        return '[{"query_success":"1"}]'
    except Exception as e:
        return '[{"query_success":"0","error":'+str(e)+'}]'

def listappoint(data):
    cust_id = data["cust_id"]

    customer = Patient.objects.filter(cust_id=cust_id)

    return Appiontment.objects.filter(cust_id=customer[0].cust_id,date__gte=datetime.date.today())
    


map2func = {
    "speclist": speclist,
    "doctlist": doctlist,
    "newappoint": newappoint,
    "changeappoint": changeappoint,
    "deleteappoint": deleteappoint,
    "listappoint": listappoint,
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

    
