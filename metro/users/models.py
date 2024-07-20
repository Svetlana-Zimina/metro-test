from django.db import models


class User(models.Model):
    """Модель Пользователь."""

    full_name = models.CharField(
        max_length=255,
        verbose_name='ФИО'
    )
    image = models.ImageField(
        upload_to='users_images',
        blank=True,
        null=True,
        verbose_name='Фото пользователя'
    )
    email = models.CharField(
        max_length=100,
        verbose_name='Электронная почта'
    )
    address = models.CharField(
        max_length=255,
        verbose_name='Адрес'
    )

    class Meta:
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.full_name
