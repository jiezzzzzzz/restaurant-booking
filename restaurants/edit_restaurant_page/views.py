from django.shortcuts import render, get_object_or_404, redirect
from user_interface.models import Place
from .forms import PostForm


def post_edit(request, id_place):
    post = get_object_or_404(Place, id_place=id_place)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm(instance=post)
    return render(request, 'user_interface/post_edit.html', {'form': form})