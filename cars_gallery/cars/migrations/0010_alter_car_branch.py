# Generated by Django 4.1.4 on 2022-12-28 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('branches', '0002_alter_branch_address_alter_branch_name_and_more'),
        ('cars', '0009_alter_car_branch_alter_car_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='branchs', related_query_name='branch', to='branches.branch'),
        ),
    ]
