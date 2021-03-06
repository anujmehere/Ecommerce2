"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings #importing settings
from django.conf.urls.static import static

urlpatterns = [
    path('' , include('accounts.urls')),
    path('wish/',include('wish.urls')),
    path('cart/',include('cart.urls')),
    path('order/',include('order.urls')),
    path('admin/', admin.site.urls),
    path('search/',include('search_app.urls')),
    path('shop/', include('shop.urls')),
    
]

if settings.DEBUG: #mapping static and media url when debug is enabled
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

    
admin.site.site_header = "Smart Retail Solutions"
admin.site.site_title = "Smart Retail Admin Portal"
admin.site.index_title = "Welcome to Smart Retail Solutions"
