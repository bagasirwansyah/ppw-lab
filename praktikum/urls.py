"""Praktikum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/lab-4/', permanent='true'), name='index'),
    path('admin/', admin.site.urls),
    path('lab-1/', include('lab_1.urls')),
    path('lab-2/', include('lab_2.urls')),
    path('lab-2-addon/', include('lab_2_addon.urls')),
    path('lab-3/', include('lab_3.urls')),
    path('lab-4/', include(('lab_4.urls', 'lab-4'), namespace='lab-4')),
]
