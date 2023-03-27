from django.urls import path
from .views import home, home_2, vote
from .views import SearchResultsView, CreateViews


urlpatterns = [
    path('', home, name='home'),
    path('search_result/', SearchResultsView.as_view(), name='search_result'),
    path('<int:id_place>/', home_2, name='restaurant_page'),
    path('favourites/', vote, name='favourites')
]