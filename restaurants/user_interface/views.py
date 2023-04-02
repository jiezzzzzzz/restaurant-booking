from django.db.models import Q
from django.shortcuts import render
from .models import Place, Street
from .forms import FilterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView
)
from .forms import PlaceFilterForm


def place_list(request):
    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            type_kitchens = form.cleaned_data['type_kitchens']
            places = Place.objects.filter(place_typekitchen__id_type__in=type_kitchens).distinct()
    else:
        form = FilterForm()
        places = Place.objects.all()
    return render(request, 'place_list.html', {'places': places, 'form': form})


class SearchResultsView(ListView):
    model = Place
    template_name = 'user_interface/search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Place.objects.filter(
            Q(name_place__icontains=query)
        )
        return object_list


class SearchResultsViewNameStreet(ListView):
    model = Street
    template_name = 'places_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Street.objects.filter(
            Q(name_street__icontains=query)
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
         'objects': [{'id': obj.id_place} for obj in object],
    }

    return render(request, 'user_interface/home.html', context)


def restaurant_page(request, id_place):
    object = Place.objects.filter(pk=id_place)
    context = {}
    for i in object:
        context = {
            'title': i.name_place,
            'id': i.id_place,
            'number_phone': i.number_phone,
            'takeaway_food': i.takeaway_food,
            'delivery': i.delivery,
            'summer_veranda': i.summer_veranda,
            'menu_vegan': i.menu_vegan,
            'visit_pet': i.visit_pet,
            'bus_lunch': i.bus_lunch,
            'child_room': i.child_room,
            'url': i.url,
            'live_music': i.live_music
        }
    return render(request, 'user_interface/restaurant_page.html', context=context)


class CreateViews(LoginRequiredMixin, CreateView):
    model = Place
    fields = ['id_place', 'name_place']

    def form_valid(self, form):
        return super().form_valid(form)


def places_list(request):
    places = Place.objects.all()
    if request.GET.get('live_music'):
        places = places.filter(live_music=True)
    if request.GET.get('takeaway_food'):
        places = places.filter(takeaway_food=True)
    if request.GET.get('delivery'):
        places = places.filter(delivery=True)
    if request.GET.get('summer_veranda'):
        places = places.filter(summer_veranda=True)
    if request.GET.get('menu_vegan'):
        places = places.filter(menu_vegan=True)
    if request.GET.get('visit_pet'):
        places = places.filter(visit_pet=True)
    if request.GET.get('bus_lunch'):
        places = places.filter(bus_lunch=True)
    if request.GET.get('child_room'):
        places = places.filter(child_room=True)
    return render(request, 'user_interface/search_list.html', {'places': places})

