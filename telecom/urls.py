from django.conf.urls import url
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('packages/<str:service_provider>/<str:payment_method>/<str:package_type>',csrf_exempt(views.packages_view)),
    path('details/<str:detail_type>/<str:service_provider>/<str:payment_method>',csrf_exempt(views.provider_specific_details_view)),
    path('complaint/',csrf_exempt(views.complaint_view)),
]

