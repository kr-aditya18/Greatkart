"""
greatkart URL Configuration
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import health_check
from . import views

urlpatterns = [
    # Health check for AWS / Load Balancer
    path('health/', health_check, name='health'),

    # Home page
    path('', views.home, name='home'),

    # Admin (honeypot + real admin)
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('securelogin/', admin.site.urls),

    # App routes
    path('store/', include('store.urls')),
    path('cart/', include('carts.urls')),
    path('accounts/', include('accounts.urls')),
    path('orders/', include('orders.urls')),
]

# Media files (only works because EB uses Nginx)
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
