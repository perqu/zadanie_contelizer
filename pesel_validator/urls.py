from django.urls import path
from .views import pesel_validation

urlpatterns = [
    path('', pesel_validation, name='home'),
]
