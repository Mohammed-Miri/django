# Generated by Django 4.1.4 on 2022-12-24 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('branches', '0002_alter_branch_address_alter_branch_name_and_more'),
        ('clients', '0003_client_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='branches.branch'),
        ),
    ]
