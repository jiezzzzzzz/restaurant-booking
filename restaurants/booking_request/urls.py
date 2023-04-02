from django.urls import path
from .views import booking_request, booking_list

urlpatterns = [
    path('<int:id_place>/', booking_request, name='booking_id'),
    path('booking_list/', booking_list, name='booking_list1')
]