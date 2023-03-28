from django.contrib import admin
from django.urls import path, include
from edit_restaurant_page.views import post_edit


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_interface.urls')),
    path('register/', include('registration.urls')),
    path('favorites/', include('favorites.urls')),
    path('booking/', include('booking_request.urls')),
    path('edit/<int:id_place>/', post_edit, name='post_edit'),
]
