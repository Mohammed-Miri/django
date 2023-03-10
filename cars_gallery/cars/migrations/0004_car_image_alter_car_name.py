# Generated by Django 4.1.4 on 2022-12-15 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_rename_cars_car_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
