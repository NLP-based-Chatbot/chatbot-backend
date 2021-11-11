from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
  path('admin/create', csrf_exempt(views.admin_view))
]