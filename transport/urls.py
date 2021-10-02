from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
  path('schedule/<str:departure>/<str:destination>', csrf_exempt(views.schedule_view))
]