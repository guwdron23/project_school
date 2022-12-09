from django.db import models

class Classes(models.Model):
    number = models.IntegerField(verbose_name='Номер класса')
    title = models.CharField(max_length=1, verbose_name='Класс')
    curator = models.CharField(max_length=25, verbose_name='Классная руководительница')

    def __str__(self):
        return self.title


