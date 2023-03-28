from django.urls import path
from .views import register, login_view, profile
from registration_manager.views import register_manager
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', register, name='register'),
    path('login/', login_view, name='login'),
    path('profile/', profile, name='profile'),
    path('manager/', register_manager, name='register_manager'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user_interface/logout.html'), name='logout'),

]
