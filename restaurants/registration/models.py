from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission, Group


class CustomUser(AbstractUser):
    id_user = models.IntegerField("Код пользователя", primary_key=True, blank=True)
    username=models.CharField("Логин", max_length=32, blank=True, unique=True)
    password=models.CharField("Пароль", max_length=64, blank=True)
    email=models.EmailField(max_length=320, blank=True)
    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        related_name='%(class)s_user_set'  # добавлен related_name
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name='%(class)s_user_set'  # добавлен related_name
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    user_type = 'User'

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural="Пользователь"

