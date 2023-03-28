from django.shortcuts import render
from .models import BookingRequest
from user_interface.models import Place
from datetime import datetime


def booking_request(request, id_place):
    object = Place.objects.filter(pk=id_place)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        guests = request.POST.get('guests')
        special_requests = request.POST.get('special_requests')
        place = Place.objects.get(id_place=id_place)
        booking_request = BookingRequest(
            id_place=place,
            id_user=request.user,
            time_visit=datetime.strptime(date, '%Y-%m-%d').date(),
            number_persons=guests,
            note_user=special_requests,
            status=False
        )

        booking_request.save()
    return render(request, 'booking_request/booking.html')
