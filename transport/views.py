from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from transport import serializer

from transport.serializer import ComplaintSerializer, OfficesSerializer, VehicalTypesSerializer
from transport.serializer import ScheduleSerializer
from transport.serializer import BookingsSerializer

from transport.models import Offices, Vehical_Types
from transport.models import Schedules
from transport.models import Bookings

from django.http import JsonResponse

# @api_view(['GET'])
def schedule_view(request, vehical_type, departure, destination):
  if request.method == 'GET':
      vehical_types = Vehical_Types.objects.filter(vehical_type=vehical_type)
      serializer_vehical_id = VehicalTypesSerializer(vehical_types, many=True)

      type_id = serializer_vehical_id.data[0]['type_id']

      schedule = Schedules.objects.filter(type_id=type_id, departure=departure, destination=destination)
      serializer_schedule = ScheduleSerializer(schedule, many=True)      
      
      return JsonResponse(serializer_schedule.data, safe=False)  

@api_view(['POST'])
def booking_view(request):
  if request.method == 'POST':
    serializer = BookingsSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET'])
def office_view(request, vehical_type, office_name, address):
  if request.method == 'GET':
    vehical_types = Vehical_Types.objects.filter(vehical_type=vehical_type)
    serializer_vehical_id = VehicalTypesSerializer(vehical_types, many=True)

    type_id = serializer_vehical_id.data[0]['type_id']   

    office = Offices.objects.filter(type_id=type_id, office_name=office_name, address=address)
    serializer_office = OfficesSerializer(office, many=True)

    return JsonResponse(serializer_office.data, safe=False)         

@api_view(['POST'])
def complaint_view(request):
  if request.method == 'POST':
    serializer = ComplaintSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  