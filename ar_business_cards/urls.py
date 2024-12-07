from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ar_business_cards.apps.landing.urls')),
    path('auth/', include('ar_business_cards.apps.accounts.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('', include('ar_business_cards.apps.core.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]
