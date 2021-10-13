from rest_framework import serializers
from rest_framework.decorators import api_view
from transport.serializer import ScheduleSerializer
from transport.models import Schedules
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser

@api_view(['GET', 'POST'])
def schedule_view(request):
  if request.method == 'GET':
      snippets = Schedules.objects().all()
      serializer = ScheduleSerializer(snippets, many=True)
      
      return JsonResponse(serializer.data, safe=False)
