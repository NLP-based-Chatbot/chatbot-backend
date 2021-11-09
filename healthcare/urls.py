from django.conf.urls import url
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

from . import views
from .dbconnection import queries

urlpatterns= [
    path('query/',csrf_exempt(queries.runquery)),
    path('report/<slug:report_filename>/',csrf_exempt(views.download_report))
]

