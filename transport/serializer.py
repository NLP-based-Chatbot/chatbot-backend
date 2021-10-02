from django.db.models import fields
from rest_framework import serializers
from transport.models import Schedules

class ScheduleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Schedules
    fields = ['mode', 'city', 'arrival']