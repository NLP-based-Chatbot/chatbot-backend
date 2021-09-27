from django.shortcuts import render
import requests
from django.http import JsonResponse


 
def assistant_healthcare(request):
    res = requests.post("http://localhost:5005/webhooks/rest/webhook",data=request.body)
    return JsonResponse(res.json())

# Create your views here.
