# Generated by Django 4.1.4 on 2022-12-16 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('cars', '0005_remove_car_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cars', related_query_name='car', to='categories.category'),
        ),
    ]
