from django.db import models
from user_interface.models import Place
from registration.models import CustomUser


class BookingRequest(models.Model):
    id_request = models.IntegerField("Код", primary_key=True)
    id_place = models.ForeignKey(Place, on_delete=models.CASCADE)
    id_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    time_visit = models.DateTimeField()
    number_persons = models.IntegerField("Количество человек")
    note_user = models.CharField("Примечание пользователя", max_length=4096)
    status = models.BooleanField()

    def __str__(self):
        return self.id_request

    class Meta:
        verbose_name = "Заявка на бронирование"
        verbose_name_plural = "Заявка на бронирование"
