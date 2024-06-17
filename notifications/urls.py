from django.urls import path
from . import views

urlpatterns = [
    path('send-async/', views.handl_user_data2, name='sync'),
    path('send-sync/', views.handl_user_data, name='async')
]