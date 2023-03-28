from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser




class TypeKitchen(models.Model):
    id_type=models.IntegerField("Номер типа кухни", primary_key=True)
    name_type= models.CharField("Наименование типа", max_length=64)

    def __str__(self):
        return self.name_type

    class Meta:
        verbose_name = "Тип кухни"
        verbose_name_plural = "Тип кухни"


class TypePlace(models.Model):
    id_type = models.IntegerField("Номер типа заведения", primary_key=True)
    name_type = models.CharField("Наименование типа заведения", max_length=64)

    def __str__(self):
        return self.name_type

    class Meta:
        verbose_name = "Тип заведения"
        verbose_name_plural = "Тип заведения"


class Street(models.Model):
    id_street = models.IntegerField("Код улицы", primary_key=True)
    name_street = models.CharField("Наименование улицы", max_length=64)

    def __str__(self):
        return self.name_street

    class Meta:
        verbose_name = "Улица"
        verbose_name_plural = "Улица"


class Place(models.Model):
    id_place = models.IntegerField("Номер заведения", primary_key=True)
    name_place = models.CharField("Наименование заведения", max_length=64)
    number_phone=models.CharField("Номер телефона", max_length=17, help_text="Формат +*(***)-***-**-**")
    id_street=models.ForeignKey("Street",to_field='id_street', on_delete=models.CASCADE)
    number_buld=models.IntegerField("Номер дома")
    id_type=models.ForeignKey("TypePlace", on_delete=models.CASCADE)
    ##
    operating_mode=models.CharField(max_length=64, null=True)
    live_music=models.BooleanField()
    takeaway_food = models.BooleanField()
    delivery = models.BooleanField()
    summer_veranda = models.BooleanField()
    menu_vegan = models.BooleanField()
    visit_pet = models.BooleanField()
    bus_lunch = models.BooleanField()
    child_room = models.BooleanField()
    features=models.JSONField()
    url=models.SlugField(null=True)

    def __str__(self):
        return self.name_place

    class Meta:
        verbose_name = "Заведения"
        verbose_name_plural = "Заведение"

    #def get_absolute_url(self):
     #   return reverse('added_new_restaurant', kwargs={'pk': self.pk})




class Place_typeKitchen(models.Model):
    id = models.IntegerField("Код", primary_key=True)
    id_place = models.ForeignKey("Place",to_field='id_place', on_delete=models.CASCADE)
    id_type = models.ForeignKey("TypeKitchen", to_field='id_type', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Заведение_типКухни"
        verbose_name_plural = "Заведение_типКухни"