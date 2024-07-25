from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    first_name = models.CharField(max_length=150, verbose_name='Имя', blank=True, null=True)
    last_name = models.CharField(max_length=150, verbose_name='Фамилия', blank=True, null=True)
    token = models.CharField(max_length=100, verbose_name='Токен', blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        permissions = [
            ("is_active", "активировать/блокировать пользователя")
        ]

    def __str__(self):
        return self.email

