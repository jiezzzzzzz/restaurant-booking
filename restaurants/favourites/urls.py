from django.urls import path
from .views import list_favorites, add_to_favorites

app_name = 'favourites'
urlpatterns = [
    path('', list_favorites, name='favorites'),
    path('add/', add_to_favorites, name='add_to_favorites'),
]