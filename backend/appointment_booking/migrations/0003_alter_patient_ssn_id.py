# Generated by Django 3.2.9 on 2021-11-06 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment_booking', '0002_auto_20211106_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='ssn_id',
            field=models.IntegerField(unique=True),
        ),
    ]