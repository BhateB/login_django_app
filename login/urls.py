"""login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from loginreg import views
from rest_framework.routers import DefaultRouter
from rest_auth.registration import *


router = DefaultRouter()
router.register(r'register', views.Register)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/', include('loginreg.urls')),
    # url(r'^login/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # url(r'^api/rest-auth/', include('rest_auth.urls')),
    url(r'^login/', include('rest_auth.urls')),
    # url(r'^rest-auth/', include('rest_auth.urls')),
    # url(r'^rest-auth/registration/', include('rest_auth.registration.urls'))
    # url(r'^api/rest-auth/registration/', include('rest_auth.registration.urls')),
    # rest framework urls
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

