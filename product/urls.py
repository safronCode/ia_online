from django.urls import path

from lobby.views import reload_lobby
from .api import autocomplete_products
from .views import qr_generator, product_card, product_catalog

urlpatterns = [
    path('generator/', qr_generator, name='qr_generator'),
    path('catalog/', product_catalog, name='catalog'),
    path('card/<slug:uuid>/', product_card, name='product_card'),
    path('autocomplete/', autocomplete_products, name='autocomplete'),
    path('',reload_lobby, name='reload_lobby')
]