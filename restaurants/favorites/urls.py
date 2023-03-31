from django.urls import path
from .views import PlaceDetailView, FavoritesListView, AddToFavoritesView

app_name = 'favorites'
urlpatterns = [
    path('', PlaceDetailView.as_view(), name='favorites'),
    path('add/<int:pk>/', AddToFavoritesView.as_view(), name='add_to_favorites')
]