from django.shortcuts import render, redirect
from .models import BookingRequest
from user_interface.models import Place
from datetime import datetime


def booking_request(request, id_place):
    place = Place.objects.get(id_place=id_place)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        guests = request.POST.get('guests')
        special_requests = request.POST.get('special_requests')
        #place = Place.objects.get(id_place=id_place)
        booking_request = BookingRequest(
            id_place=place,
            id_user=request.user,
            time_visit=datetime.strptime(date, '%Y-%m-%d').date(),
            number_persons=guests,
            note_user=special_requests,
            status=False
        )

        BookingRequest.objects.create(id_place=place,
            id_user=request.user,
            time_visit=datetime.strptime(date, '%Y-%m-%d').date(),
            number_persons=guests,
            note_user=special_requests,
            status=False)
        return redirect('home')

    return render(request, 'booking_request/booking.html', {'place': place})


def booking_list(request):
    # Получаем все объекты из модели BookingRequest, которые относятся к текущему пользователю
    booking_objects = BookingRequest.objects.filter(id_user=request.user)
    place = Place.objects.get()
    # Отображаем список избранных элементов на странице
    return render(request, 'booking_request/booking_list.html', {'booking_objects': booking_objects, 'place': place})