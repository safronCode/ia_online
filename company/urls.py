from django.urls import path
from .views import company_map
from lobby.views import reload_lobby

urlpatterns = [
    path('map/', company_map, name='company_map'),
    path('', reload_lobby, name='reload_lobby')
]
