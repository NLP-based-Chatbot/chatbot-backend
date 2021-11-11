from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
  path('schedule/<str:vehical_type>/<str:departure>/<str:destination>', csrf_exempt(views.schedule_view)),
  path('booking', csrf_exempt(views.booking_view)),
  path('office/<str:vehical_type>/<str:office_name>/<str:address>', csrf_exempt(views.office_view)),
  path('complaint', csrf_exempt(views.complaint_view))
]