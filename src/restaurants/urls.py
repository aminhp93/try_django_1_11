from django.conf.urls import url

from .views import (    
    restaurant_listview,
    restaurant_createview,
    RestaurantListView,
    RestaurantDetailView,
    RestaurantCreateView,
    RestaurantUpdateView
    )

urlpatterns = [
    
    # url(r'^/(?P<slug>[\w-]+)/$', RestaurantListView.as_view()),
    # url(r'^/create/$', restaurant_createview),
    url(r'^create/$', RestaurantCreateView.as_view(), name='create'),
    # url(r'^(?P<slug>[\w-]+)/edit/$', RestaurantUpdateView.as_view(), name='edit'),
    url(r'^(?P<slug>[\w-]+)/$', RestaurantUpdateView.as_view(), name='detail'),
    url(r'$', RestaurantListView.as_view(), name='list'),
]
