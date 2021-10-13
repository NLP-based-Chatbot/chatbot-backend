from rest_framework.decorators import api_view
from telecom.serializer import PackageSerializer
from telecom.models import Packages
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser

@api_view(['GET', 'POST'])
def packages_view(request, service_provider, payment_method, package_type):
    if request.method == 'GET':
      snippets = Packages.objects.filter(service_provider=service_provider, payment_method=payment_method, package_type=package_type)
      serializer = PackageSerializer(snippets, many=True)
      
      return JsonResponse(serializer.data, safe=False)
