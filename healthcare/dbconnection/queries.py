from django.shortcuts import render
import requests
from django.http import JsonResponse,HttpResponse
from django.core import serializers
import json

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


    
def speclist():
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

def changeappoint():
    pass

def deleteappoint():
    pass

def listappoint():
    pass