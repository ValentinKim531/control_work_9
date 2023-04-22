from django.db import models

from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    name = models.CharField(max_length=150, null=False, blank=False, verbose_name='Имя')
    phone = models.CharField(max_length=12, verbose_name='Телефон', null=True, blank=True)
    favorited_photos = models.ManyToManyField(
        to='webapp.Gallery',
        through='webapp.Favorite',
        related_name='favorited_users',
        verbose_name='Избранные фото'
        )

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
    
    def __str__(self):
        return self.name
