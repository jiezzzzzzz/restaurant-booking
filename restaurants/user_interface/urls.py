from django.urls import path
from .views import start_page, home


urlpatterns = [
    path('', start_page),
    path('home/', home)
]