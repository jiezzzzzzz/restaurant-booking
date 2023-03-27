from django.db import models
from user_interface.models import Place
from registration.models import AbstractniyUser
class Favorites(models.Model):
    id_favorites=models.IntegerField("Код", primary_key=True)
    id_place = models.ForeignKey(Place, on_delete=models.CASCADE)
    id_user = models.ForeignKey(AbstractniyUser, on_delete=models.CASCADE)
    page_url = models.URLField()

    def __str__(self):
        return self.page_url

    class Meta:
        verbose_name = "Избранное"
        verbose_name_plural = "Избранное"
