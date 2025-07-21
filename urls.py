from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from start.views import start


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', start, name='start'),
    path('lobby/', include('lobby.urls')),
    path('deals/', include('deals.urls')),
    path('product/', include('product.urls')),
    path('staff/', include('staff.urls')),
    path('company/', include('company.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)