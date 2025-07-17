from django.urls import path

from lobby.views import reload_lobby
from .views import employees_telephony, call_generator

urlpatterns = [
    path('telephony/', employees_telephony, name='telephony'),
    path('generate_calls/', call_generator, name='call_generator'),
    path('', reload_lobby, name='reload_lobby')
]