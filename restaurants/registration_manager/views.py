from django.shortcuts import render, redirect
from .forms import ManagerRegistrationForm
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404
from booking_request.models import BookingRequest
from .forms import BookingRequestForm


def register_manager(request):
    if request.method == 'POST':
        form = ManagerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ManagerRegistrationForm()
    return render(request, 'registration/register_manager.html', {'form': form})


@user_passes_test(lambda u: u.is_authenticated and u.user_type == 'Manager')
def booking_request_list(request):
    booking_requests = BookingRequest.objects.all()
    if request.method == 'POST':
        form = BookingRequestForm(request.POST)
        if form.is_valid():
            booking_request = get_object_or_404(BookingRequest, id_request=form.cleaned_data['id_request'])
            booking_request.status = form.cleaned_data['status']
            booking_request.save()
    else:
        form = BookingRequestForm()
    return render(request, 'booking_request/booking_request_list.html', {'booking_requests': booking_requests, 'form': form})
