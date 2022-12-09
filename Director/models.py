from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=10, verbose_name='Имя')
    sur_name = models.CharField(max_length=15, verbose_name='Фамилия')
    image = models.ImageField(upload_to='media/', blank=True, null=True, verbose_name='Фото')
    phone = models.CharField(max_length=12, unique=True, verbose_name='Номер')

    @property
    def full_name(self):
        return f"{self.name} {self.sur_name}"

    def save(self, *args, **kwarg):
        self.phone = self.phone.replace(' ', '')
        super().save(*args, **kwarg)

    def __str__(self):
        return str(self.name) + '' + str(self.sur_name)

    class Meta:
        verbose_name = 'Director'
        verbose_name_plural = 'Директор'
