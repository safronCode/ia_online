from tkinter.font import names

from django.urls import path

from .views import import_contacts, export_contacts
from lobby.views import reload_lobby


urlpatterns = [
    path('import/', import_contacts, name='import_contacts'),
    path('export/', export_contacts, name='export_contacts'),
    path('', reload_lobby, name='reload_lobby')
]