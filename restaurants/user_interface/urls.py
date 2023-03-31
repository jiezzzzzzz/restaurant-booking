from django.urls import path
from .views import home, restaurant_page, places_list
from .views import SearchResultsView, SearchResultsViewNameStreet


urlpatterns = [
    path('', home, name='home'),
    path('search_result/', SearchResultsView.as_view(), name='search_result'),
    path('<int:id_place>/', restaurant_page, name='restaurant_page'),
    path('places_list/', SearchResultsViewNameStreet.as_view(), name='search_street'),
    path('search_list/', places_list, name='places_list')
]