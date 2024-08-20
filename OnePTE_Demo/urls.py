"""
URL configuration for OnePTE_Demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from accounts import urls as accounts_urls
from spoken_test import urls as sst_urls
from reorder_paragraph import urls as ro_urls
from reading_multiple_choice import urls as rrmcq_urls
from OnePTE_Demo.view import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(sst_urls,namespace='spoken_test')),
    path('',include(ro_urls,namespace='reorder_paragraph')),
    path('',include(rrmcq_urls,namespace='reading_multiple_choice')),
    path('accounts/', include(accounts_urls,namespace='accounts')),
    path('home', home, name='home'),
]
