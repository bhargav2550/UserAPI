# Generated by Django 4.2.3 on 2023-07-14 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]
