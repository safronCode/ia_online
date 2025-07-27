from django.urls import path

from .api import autocomplete_companies
from lobby.views import reload_lobby
from .views import import_contacts, export_contacts


urlpatterns = [
    path('import/', import_contacts, name='import_contacts'),
    path('export/', export_contacts, name='export_contacts'),
    path('autocomplete/', autocomplete_companies, name='autocomplete'),
    path('', reload_lobby, name='reload_lobby')
]