from django.conf.urls import url
from django.urls import path, include, re_path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('healthcare/',views.assistant_healthcare)
]

