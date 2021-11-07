from rest_framework import serializers
from telecom.models import Complaint, Packages, ProviderSpecificDetails
class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packages
        fields = ['service_provider', 'payment_method', 'package_type', 'package_name', 'value', 'description', 'activation_method']

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = ['title', 'description', 'name', 'contact_no', 'email']

class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderSpecificDetails
        fields = ['detail_type', 'provider', 'payment_method', 'description']