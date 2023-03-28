from django.shortcuts import render, get_object_or_404, redirect
from user_interface.models import Place
from .forms import PostForm
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import PostForm


def manager_only(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_type == 'Manager':
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return wrapper

@login_required
@manager_only
def post_edit(request, post_id):
    post = get_object_or_404(Place, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('home'))
    else:
        form = PostForm(instance=post)
        return render(request, 'user_interface/post_edit.html', {'form': form})