from django.db.models import fields
from rest_framework import serializers
from transport.models import Vehical_Types
from transport.models import Schedules
from transport.models import Bookings
from transport.models import Offices
from transport.models import Complaints

class VehicalTypesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Vehical_Types
    fields = '__all__'  

class ScheduleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Schedules
    fields = '__all__'

class BookingsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Bookings
    fields = '__all__'

class OfficesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Offices
    fields = '__all__' 

class ComplaintSerializer(serializers.ModelSerializer):
  class Meta:
    model = Complaints
    fields = '__all__'  