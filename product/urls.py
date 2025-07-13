from django.urls import path

from .views import qr_generator, product_card, product_catalog
from lobby.views import reload_lobby

urlpatterns = [
    path('generator/', qr_generator, name='qr_generator'),
    path('catalog/', product_catalog, name='catalog'),
    path('card/<slug:uuid>/', product_card, name='product_card'),
    path('',reload_lobby, name='reload_lobby')
]