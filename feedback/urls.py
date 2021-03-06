from django.conf.urls import url
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('',csrf_exempt(views.feedback_view)),
    path('update/<int:pk>', csrf_exempt(views.feedback_update_view))
]

