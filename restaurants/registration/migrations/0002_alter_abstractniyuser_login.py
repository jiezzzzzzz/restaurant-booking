# Generated by Django 4.1.7 on 2023-03-27 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstractniyuser',
            name='login',
            field=models.CharField(blank=True, max_length=32, unique=True, verbose_name='Логин'),
        ),
    ]
