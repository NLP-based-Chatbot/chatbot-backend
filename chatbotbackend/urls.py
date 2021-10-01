from django.conf.urls import url
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('assistant/',include('chatbotportal.urls')),
    path('feedback/', include('feedback.urls')),
    path('healthcare/',include('healthcare.urls')),
    path('telecom/',include('telecom.urls')),
    path('transport/',include('transport.urls')),
]

