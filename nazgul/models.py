from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    email = models.EmailField(verbose_name='Почта')
    message = models.TextField()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'