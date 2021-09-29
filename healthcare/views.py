from django.shortcuts import render
import requests
from django.http import JsonResponse,HttpResponse
import json


def runquery(request):
    querydata=request.body
    querydata_dict = json.load(querydata)

    


    

# Create your views here.
