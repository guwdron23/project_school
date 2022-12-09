from django.db import models


from .utils import validate_phone_number, validate_klas

class Student(models.Model):
    fio = models.CharField(max_length=255, verbose_name='ФИО')
    klass = models.PositiveIntegerField(verbose_name="Класс", validators=[validate_klas])
    phone_parent = models.CharField(max_length=55, unique=True,
                             validators=[validate_phone_number],
                             verbose_name='Номер Родителей',
                             help_text='Номер должен содержать междкнародный формат')
    live = models.CharField(max_length=255, verbose_name="Место проживания")
    image = models.ImageField(upload_to='news/', verbose_name="Изоброжение",blank=True,null=True)


    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'