from django.contrib import admin
from .models import TypeKitchen, TypePlace, Street, Place, Place_typeKitchen


admin.site.register(TypeKitchen)
admin.site.register(TypePlace)
admin.site.register(Street)
admin.site.register(Place)
admin.site.register(Place_typeKitchen)

