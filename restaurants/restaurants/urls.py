"""restaurants URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from edit_restaurant_page.views import post_edit
from django.contrib.auth.decorators import user_passes_test


def is_manager(user):
    return user.is_authenticated and user.groups.filter(name='Manager').exists()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_interface.urls')),
    path('register/', include('registration.urls')),
    path('favorites/', include('favourites.urls')),
    path('booking/', include('booking_request.urls')),
    path('edit/<int:id_place>/', post_edit, name='post_edit'),
]
