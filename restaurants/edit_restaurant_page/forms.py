from django import forms
from user_interface.models import Place


class PostForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('name_place', 'number_phone', 'live_music', 'takeaway_food', 'delivery', 'summer_veranda',
                  'menu_vegan', 'visit_pet', 'bus_lunch', 'child_room', 'features', 'url')