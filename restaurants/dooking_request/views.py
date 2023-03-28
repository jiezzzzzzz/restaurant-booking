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
        object = Place.objects.filter(pk=id_place)
        context = {}
        for i in object:
            context = {
                'id': i.id_place,
            }
        place = Place.objects.get(id_place=id_place)
        # Создаем объект BookingRequest
        booking_request = BookingRequest(
            id_place=place,  # Здесь нужно указать объект Place, для которого происходит бронирование
            id_user=request.user,  # Здесь нужно указать текущего пользователя
            time_visit=datetime.strptime(date, '%Y-%m-%d').date(),
            number_persons=guests,
            note_user=special_requests,
            status=False  # По умолчанию статус заявки False, т.е. не подтверждена
        )

        # Сохраняем объект в базу данных
        booking_request.save()
    return render(request, 'boorking_request/booking.html', context)
