from django.conf.urls import url
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns=[
    path('query/',csrf_exempt(views.runquery))
]