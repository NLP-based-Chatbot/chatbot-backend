from telecom.serializer import ComplaintSerializer, DetailsSerializer, PackageSerializer
from telecom.models import Packages, ProviderSpecificDetails
from rest_framework.decorators import api_view
from telecom.serializer import PackageSerializer
from telecom.models import Packages
from django.shortcuts import render
import requests
from django.http import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser


def runquery(request):
    querydata=request.body
    

@api_view(['GET', 'POST'])
def packages_view(request, service_provider, payment_method, package_type):
  if request.method == 'GET':
    snippets = Packages.objects.filter(service_provider=service_provider, payment_method=payment_method, package_type=package_type)
    serializer = PackageSerializer(snippets, many=True)
    
    return JsonResponse(serializer.data, safe=False)

def complaint_view(request):
  if request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = ComplaintSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

def provider_specific_details_view(request, detail_type, service_provider, payment_method):
  if request.method == 'GET':
    if payment_method == "none":
      snippets = ProviderSpecificDetails.objects.filter(provider=service_provider, detail_type=detail_type)
    else:
      snippets = ProviderSpecificDetails.objects.filter(provider=service_provider, detail_type=detail_type, payment_method=payment_method)
    
    serializer = DetailsSerializer(snippets, many=True)
    return JsonResponse(serializer.data, safe=False)