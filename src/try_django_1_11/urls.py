"""try_django_1_11 URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from restaurants.views import (
    AboutTemplateView, 
    HomeTemplateView, 
    ContactTemplateView,
    restaurant_listview,
    restaurant_createview,
    RestaurantListView,
    RestaurantDetailView,
    RestaurantCreateView
    )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeTemplateView.as_view()),
    url(r'^restaurants/$', RestaurantListView.as_view()),
    # url(r'^restaurants/(?P<slug>[\w-]+)/$', RestaurantListView.as_view()),
    # url(r'^restaurants/create/$', restaurant_createview),
    url(r'^restaurants/create/$', RestaurantCreateView.as_view()),
    url(r'^restaurants/(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view()),

    url(r'^about/$', AboutTemplateView.as_view()),
    url(r'^contact/(?P<id>\d+)/$', ContactTemplateView.as_view()),
]
