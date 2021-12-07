from django.shortcuts import render
import requests
from django.http import JsonResponse,HttpResponse
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def assistant_healthcare(request):
    res = requests.post("http://localhost:5005/webhooks/rest/webhook",data=request.body)
    return HttpResponse(res)

@api_view(['GET', 'POST'])
def assistant_transport(request):
    res = requests.post("http://localhost:5015/webhooks/rest/webhook",data=request.body)
    return HttpResponse(res)

@api_view(['GET', 'POST'])
def assistant_telecommunication(request):
    res = requests.post("http://localhost:5025/webhooks/rest/webhook",data=request.body)
    return HttpResponse(res)

# Create your views here.
