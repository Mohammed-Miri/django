# Generated by Django 4.1.4 on 2022-12-23 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='amount',
        ),
    ]
