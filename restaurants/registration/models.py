from django.db import models
from django.contrib.auth.models import AbstractUser


class AbstractniyUser(AbstractUser):
    id_user = models.IntegerField("Код пользователя", primary_key=True, blank=True)
    username=models.CharField("Логин", max_length=32, blank=True, unique=True)
    password=models.CharField("Пароль", max_length=64, blank=True)
    email=models.EmailField(max_length=320, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural="Пользователь"

