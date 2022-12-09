# Generated by Django 4.1.4 on 2022-12-09 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Имя')),
                ('sur_name', models.CharField(max_length=15, verbose_name='Фамилия')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Фото')),
                ('phone', models.CharField(max_length=12, unique=True, verbose_name='Номер')),
            ],
            options={
                'verbose_name': 'Director',
                'verbose_name_plural': 'Директор',
            },
        ),
    ]