from subprocess import Popen

from django.shortcuts import render
from rest_framework import status
from rest_framework import response
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['POST'])
def admin_view(request):
  if request.method == 'POST':
    data = request.data

    email = data['email']
    first_name = data['first_name']
    last_name = data['last_name']
    password = data['password']

    # running the script to create a superuser
    # p1 = subprocess.run(f'python manage.py createsuperuser --email {email} --first_name {first_name} --last_name {last_name}', text=True, shell=True)
    # print(p1.communicate())

    p1 = Popen(f'python manage.py createsuperuser --email {email} --first_name {first_name} --last_name {last_name} --password {password}', shell=True)

    return Response(status=status.HTTP_201_CREATED)
