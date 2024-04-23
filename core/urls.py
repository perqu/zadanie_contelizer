from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('text/', include('text_processing.urls')),
    path('pesel/', include('pesel_validator.urls')),
]
