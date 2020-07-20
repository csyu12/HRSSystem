"""HLSSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('accounts/', include(('app_accounts.urls', 'app_accounts'), namespace='app_accounts')),
    path('contacts/', include(('app_contacts.urls', 'app_contacts'), namespace='app_contacts')),
    path('listings/', include(('app_listings.urls', 'app_listings'), namespace='app_listings')),
    path('', include(('app_pages.urls', 'app_pages'), namespace='app_pages')),
    path('admin/', admin.site.urls),
]
