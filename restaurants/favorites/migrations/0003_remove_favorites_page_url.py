# Generated by Django 4.1.7 on 2023-03-31 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favorites', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorites',
            name='page_url',
        ),
    ]
