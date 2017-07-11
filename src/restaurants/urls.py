from django.conf.urls import url

from .views import (    
    restaurant_listview,
    restaurant_createview,
    RestaurantListView,
    RestaurantDetailView,
    RestaurantCreateView
    )

urlpatterns = [
    url(r'$', RestaurantListView.as_view(), name='list'),
    # url(r'^/(?P<slug>[\w-]+)/$', RestaurantListView.as_view()),
    # url(r'^/create/$', restaurant_createview),
    url(r'^create/$', RestaurantCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(), name='detail'),
]
