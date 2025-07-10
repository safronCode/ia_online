from django.urls import path
from .views import reload_lobby



urlpatterns = [
    path('', reload_lobby, name='reload_lobby')
]
