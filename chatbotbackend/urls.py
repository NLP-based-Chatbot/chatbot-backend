from django.conf.urls import url
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('assistant/',include('chatbotportal.urls')),
    path('feedback/', include('feedback.urls')),
    path('packages/', include('telecom.urls'))
]

