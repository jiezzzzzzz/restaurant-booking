from django.contrib import admin
from .models import User, TypeKitchen, TypePlace, Street, Place, Manager, Place_typeKitchen, Favorites, BookingRequest
from django.contrib.auth.models import Group


admin.site.register(User)
admin.site.register(TypeKitchen)
admin.site.register(TypePlace)
admin.site.register(Street)
admin.site.register(Place)
admin.site.register(Manager)
admin.site.register(Place_typeKitchen)
admin.site.register(Favorites)
admin.site.register(BookingRequest)

manager_group, created = Group.objects.get_or_create(name='Manager')
manager_group.user_permissions.all()