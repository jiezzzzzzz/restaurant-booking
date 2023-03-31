from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission, Group
from user_interface.models import Place


class Manager(AbstractUser):
    id_manager = models.IntegerField("Код менеджера", primary_key=True)
    place_id = models.ForeignKey(Place, on_delete=models.CASCADE)
    login = models.CharField("Логин", max_length=32, unique=True)
    password = models.CharField("Пароль", max_length=64)
    email = models.EmailField(max_length=320)
    surname = models.CharField("Фамилия", max_length=43 )
    name = models.CharField("Имя", max_length=16)
    patronymic = models.CharField("Отчество", max_length=20)

    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='manager_user_set'  # добавлен related_name
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name='manager_user_set'
    )
    user_type = 'Manager'

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = "Менеджер"
        verbose_name_plural = "Менеджер"
