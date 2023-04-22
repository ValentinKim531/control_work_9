from django.contrib.auth import get_user_model
from django.db import models


class Gallery(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        max_length=50,
        related_name='author',
        verbose_name="Автор"
    )
    photo = models.ImageField(upload_to='user_pic', verbose_name='Фото')
    signature = models.CharField(
        max_length=150, null=False,
        blank=False,
        verbose_name='Подпись'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время создания"
    )

    class Meta():
        ordering = ['-created_at']


