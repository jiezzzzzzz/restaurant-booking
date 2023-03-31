# Generated by Django 4.1.7 on 2023-03-31 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_customuser_place_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=320, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(blank=True, max_length=32, verbose_name='Логин'),
        ),
    ]