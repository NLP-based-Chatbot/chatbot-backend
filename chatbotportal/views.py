from django.shortcuts import render
import requests
from django.http import JsonResponse,HttpResponse

 
def assistant_healthcare(request):
    res = requests.post("http://localhost:5005/webhooks/rest/webhook",data=request.body)
    return HttpResponse(res)

def assistant_transport(request):
    res = requests.post("http://localhost:5015/webhooks/rest/webhook",data=request.body)
    return HttpResponse(res)

def assistant_telecommunication(request):
    res = requests.post("http://localhost:5025/webhooks/rest/webhook",data=request.body)
    return HttpResponse(res)

# Create your views here.
