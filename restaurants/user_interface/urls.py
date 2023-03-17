from django.urls import path
from .views import start_page, home
from .views import SearchResultsView


urlpatterns = [
    path('', start_page),
    path('home/', home),
    path('search_result/', SearchResultsView.as_view(), name='search_result')
]