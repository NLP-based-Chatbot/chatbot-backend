from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from transport.serializer import ComplaintSerializer, OfficesSerializer, VehicalTypesSerializer, ScheduleSerializer, BookingsSerializer
from transport.models import Offices, Vehical_Types, Schedules

from django.http import JsonResponse

def runquery(request):
  querydata = request.body

def schedule_view(request, vehical_type, departure, destination):
  if request.method == 'GET':
      vehical_types = Vehical_Types.objects.filter(vehical_type=vehical_type)
      serializer_vehical_id = VehicalTypesSerializer(vehical_types, many=True)

      type_id = serializer_vehical_id.data[0]['type_id']

      schedule = Schedules.objects.filter(type_id=type_id, departure=departure, destination=destination)
      serializer_schedule = ScheduleSerializer(schedule, many=True)      
      
      return JsonResponse(serializer_schedule.data, safe=False)  

def booking_view(request):
  if request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = BookingsSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

def office_view(request, vehical_type, office_name, address):
  if request.method == 'GET':
    vehical_types = Vehical_Types.objects.filter(vehical_type=vehical_type)
    serializer_vehical_id = VehicalTypesSerializer(vehical_types, many=True)

    type_id = serializer_vehical_id.data[0]['type_id']   
    
    office = Offices.objects.filter(type_id=type_id, office_name=office_name, address=address)
    serializer_office = OfficesSerializer(office, many=True)

    return JsonResponse(serializer_office.data, safe=False)         

def complaint_view(request):
  if request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = ComplaintSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  