from django.urls import path

from .views import active_deals, add_deal
from lobby.views import reload_lobby

urlpatterns = [
    path('active/', active_deals, name='active_deals'),
    path('add/', add_deal, name='add_deal'),
    path('', reload_lobby, name='reload_lobby')
]
