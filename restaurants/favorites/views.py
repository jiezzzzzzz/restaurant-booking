from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Favorites
from registration.models import CustomUser
from user_interface.models import Place


@csrf_exempt
def add_to_favorites(request):
    if request.method == 'POST':
        place_id = request.POST.get('id_place')
        user_id = request.POST.get('id_user')
        place = get_object_or_404(Place, id=place_id)
        user = get_object_or_404(CustomUser, id=user_id)
        Favorites.objects.create(id_place=place_id, id_user=user_id)
        return JsonResponse({'status': 'ok'})


def list_favorites(request):
    fav = Favorites.objects.all()
    return render(request, 'favorites/list_favorite.html', {'objects': fav})

