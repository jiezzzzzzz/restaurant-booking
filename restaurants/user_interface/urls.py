from django.urls import path
from .views import home, restaurant_page
from .views import SearchResultsView


urlpatterns = [
    path('', home, name='home'),
    path('search_result/', SearchResultsView.as_view(), name='search_result'),
    path('<int:id_place>/', restaurant_page, name='restaurant_page'),
]