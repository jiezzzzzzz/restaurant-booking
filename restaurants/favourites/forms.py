from django import forms
from .models import Favorites

class FavoriteForm(forms.ModelForm):
    class Meta:
        model = Favorites
        fields = ['page_url']