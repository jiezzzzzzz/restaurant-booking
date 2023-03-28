from django.urls import path
from .views import register, login_view, profile

urlpatterns = [
    path('', register, name='register'),
    path('login/', login_view, name='login'),
    path('profile/', profile, name='profile'),
]
