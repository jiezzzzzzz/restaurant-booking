from django.urls import path
from .views import home, home_2
from .views import SearchResultsView


urlpatterns = [
    path('', home, name='home'),
    path('search_result/', SearchResultsView.as_view(), name='search_result'),
    path('<int:id_place>/', home_2, name='restaurant_page')
]