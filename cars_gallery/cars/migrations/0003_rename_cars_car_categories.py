# Generated by Django 4.1.4 on 2022-12-13 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_remove_car_model'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='cars',
            new_name='categories',
        ),
    ]
