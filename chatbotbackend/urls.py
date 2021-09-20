from django.conf.urls import url
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.jwt'))
]

