from django.db import models
from teachers.models import Teachers


class Lessons(models.Model):
    name_lessons = models.CharField(max_length=55, verbose_name='Название урока')
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE, verbose_name='Учитель')

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'