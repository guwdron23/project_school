# Generated by Django 4.1.4 on 2022-12-09 07:42

from django.db import migrations, models
import zavuch.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zavuch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=55, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=55, verbose_name='Фамилия')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Фото завуча')),
                ('phone', models.CharField(help_text='Номер должен быть на международном формате!', max_length=12, unique=True, validators=[zavuch.utils.validate_phone_namber], verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Завуч',
                'verbose_name_plural': 'Завучи',
            },
        ),
    ]
