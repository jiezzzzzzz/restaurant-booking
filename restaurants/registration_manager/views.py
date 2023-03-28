from django.shortcuts import render, redirect
from .forms import ManagerRegistrationForm


def register_manager(request):
    if request.method == 'POST':
        form = ManagerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ManagerRegistrationForm()
    return render(request, 'registration/register_manager.html', {'form': form})
