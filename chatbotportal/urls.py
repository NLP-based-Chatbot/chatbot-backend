from django.conf.urls import url
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('healthcare/',csrf_exempt(views.assistant_healthcare)),
    path('transport/',csrf_exempt(views.assistant_transport(request))),
    path('telecom/',csrf_exempt(views.assistant_telecommunication(request))),
]

