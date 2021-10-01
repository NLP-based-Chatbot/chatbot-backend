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

    if spec_id == None:
        return Doctor.objects.all()
    
    return Doctor.objects.filter(DoctorSpec__spec_id=spec_id)
    

def newappoint(data):
    doct_id = data["spec_id"]
    cust_id = data["cust_id"]
    date = data["date"]
    time = data["time"]

    new_appointment = Appiontment(doctor_id=doct_id, cust_id=cust_id,date=date,time_slot=time)

    try:
        new_appointment.save()
        return json.loads('{"query_success":"1"}')
    except Exception:
        return json.loads('{"query_success":"0"}')



def changeappoint(data):
    appoint_id = data["appoint_id"]
    date = data["date"]
    time = data["time"]

    alt_appointment = Appiontment.objects.get(appointment_id=appoint_id)

    alt_appointment.date=date
    alt_appointment.time_slot=time

    try:
        alt_appointment.save()
        return json.loads('{"query_success":"1"}')
    except Exception:
        return json.loads('{"query_success":"0"}')

def deleteappoint(data):
    appoint_id = data["appoint_id"]

    del_appointment = Appiontment.objects.get(appointment_id=appoint_id)

    try:
        del_appointment.delete()
        return json.loads('{"query_success":"1"}')
    except Exception:
        return json.loads('{"query_success":"0"}')

def listappoint(data):
    userhash = data["userhash"]

    customer = Patient.objects.filter(userhash=userhash)

    return Appiontment.objects.filter(cust_id=customer.cust_id,date__gte=datetime.date.today())
    


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

    func_to_exc = querydata["function"]

    result = func_to_exc(querydata["data"])

    try:
        result_json = serializers.serialize('json', result)
    except Exception:
        result_json = result

    return HttpResponse(result_json, content_type='application/json')

    
