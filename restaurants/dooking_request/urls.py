from django.urls import path
from .views import booking_request

urlpatterns = [
    path('<int:id_place>/', booking_request, name='booking_id')
]