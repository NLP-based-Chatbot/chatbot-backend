from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('news/domain/<str:domain>',csrf_exempt(views.news_list)),
    path('news/details/<str:pk>',csrf_exempt(views.news_detail)),
    path('news/',csrf_exempt(views.news_view)),
    path('instructions/domain/<str:domain>',csrf_exempt(views.instructions_list)),
    path('instructions/details/<str:pk>',csrf_exempt(views.instructions_detail)),
    path('instructions/',csrf_exempt(views.instructions_view)),
]

