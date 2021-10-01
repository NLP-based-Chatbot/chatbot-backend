from django.shortcuts import render
import requests
from django.http import JsonResponse,HttpResponse
from django.core import serializers
import json

from healthcare import models

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
    querydata_dict = json.load(querydata)

    func_to_exc = querydata["function"]

    result = func_to_exc(querydata)
    result_json = serializers.serialize('json', result)

    return HttpResponse(result_json, content_type='application/json')

    
def speclist(data):
    pass

def doctlist(data):
    try:
        spec_id = data["spec_id"]
    except KeyError:
        spec_id = None
    

    pass

def newappoint(data):
    doct_id = data["spec_id"]
    cust_id = data["cust_id"]
    date = data["date"]
    time = data["time"]
    pass

def changeappoint(data):
    appoint_id = data["appoint_id"]
    date = data["date"]
    time = data["time"]
    pass

def deleteappoint(data):
    appoint_id = data["appoint_id"]
    pass

def listappoint(data):
    cust_id = data["cust_id"]
    pass