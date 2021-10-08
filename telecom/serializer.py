from rest_framework import serializers
from telecom.models import Packages
class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packages
        fields = ['service_provider', 'payment_method', 'package_type', 'package_name', 'value', 'description', 'activation_method']