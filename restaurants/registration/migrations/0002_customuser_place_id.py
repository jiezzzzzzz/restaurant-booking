# Generated by Django 4.1.7 on 2023-03-31 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_interface', '0001_initial'),
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='place_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_interface.place'),
            preserve_default=False,
        ),
    ]
