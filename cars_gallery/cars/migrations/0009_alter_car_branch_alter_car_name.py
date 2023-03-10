# Generated by Django 4.1.4 on 2022-12-24 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('branches', '0002_alter_branch_address_alter_branch_name_and_more'),
        ('cars', '0008_car_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='branches.branch'),
        ),
        migrations.AlterField(
            model_name='car',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]
