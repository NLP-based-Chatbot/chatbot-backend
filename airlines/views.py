from django.shortcuts import render
import requests
from django.http import JsonResponse,HttpResponse


def runquery(request):
    querydata=request.body
    

# Create your views here.
