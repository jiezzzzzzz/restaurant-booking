from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView
from .models import Place
from django.shortcuts import get_object_or_404


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
    context = {}
    for i in object:
        context = {
            'title': i.name_place,
            'id': i.id_place,
        }
    return render(request, 'user_interface/home.html', {'objects': object})


def home_2(request, id_place):
    object = Place.objects.filter(pk=id_place)
    context = {}
    for i in object:
        context = {
            'title': i.name_place,
            'id': i.id_place,
        }
    return render(request, 'user_interface/restaurant_page.html', context=context)



def start_page(request):
    return render(request, 'user_interface/about.html')
