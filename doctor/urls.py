# doctor/urls.py
from django.urls import path
from .views import doctor_list_create_view,login_api_view

urlpatterns = [
    path('signup/', doctor_list_create_view, name='doctor-list-create'),
    path('login/', login_api_view, name='api-login'),
]
