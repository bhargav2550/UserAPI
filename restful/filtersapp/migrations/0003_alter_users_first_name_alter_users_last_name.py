# Generated by Django 4.2.3 on 2023-07-17 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filtersapp', '0002_alter_users_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='first_name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='users',
            name='last_name',
            field=models.CharField(max_length=40),
        ),
    ]
