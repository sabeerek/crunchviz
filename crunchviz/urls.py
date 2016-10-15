"""crunchviz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from crunch.views import view_by_category,view_by_location, index,get_by_category

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^view-by-category/', view_by_category),
    url(r'^view-by-location/', view_by_location),
    url(r'^get_by_category/', get_by_category),
    url(r'^$', index),
]