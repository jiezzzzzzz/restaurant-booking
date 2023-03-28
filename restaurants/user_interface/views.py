from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Place
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView
)

from .forms import PlaceFilterForm


class SearchResultsView(ListView):
    model = Place
    template_name = 'user_interface/search_result.html'


    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Place.objects.filter(
            Q(name_place__icontains=query)
        )
        return object_list


def home(request):
    object = Place.objects.all()
    form = PlaceFilterForm(request.GET or None)

    if form.is_valid():
        places = form.filter_places()
    else:
        places = Place.objects.all()

    context = {
        'form': form,
        'places': places,
        'objects': object
    }

    return render(request, 'user_interface/home.html', context)


def home_2(request, id_place):
    object = Place.objects.filter(pk=id_place)
    context = {}
    for i in object:
        context = {
            'title': i.name_place,
            'id': i.id_place,
        }
    return render(request, 'user_interface/restaurant_page.html', context=context)


class CreateViews(LoginRequiredMixin, CreateView):
    model = Place
    fields = ['id_place', 'name_place']

    def form_valid(self, form):
        return super().form_valid(form)

