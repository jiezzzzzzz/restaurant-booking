from django import forms
from .models import Place, TypePlace


class PlaceFilterForm(forms.Form):
    type_place = forms.ModelMultipleChoiceField(
        queryset=TypePlace.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Тип заведения',
        required=False
    )

    def filter_places(self):
        places = Place.objects.all()

        if self.cleaned_data['type_place']:
            places = places.filter(id_type__in=self.cleaned_data['type_place'])

        return places

