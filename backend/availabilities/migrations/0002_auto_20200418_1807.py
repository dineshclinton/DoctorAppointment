# Generated by Django 3.0 on 2020-04-18 18:07

from datetime import date, time

from django.db import migrations


def seed_availabilities_for_today(apps, schema_editor):
    Availability = apps.get_model("availabilities", "Availability")
    today = date.today()
    times_of_day = [
        [9, 0],
        [9, 30],
        [10, 0],
        [10, 30],
        [13, 0],
        [13, 30],
        [14, 00],
        [14, 30],
        [15, 00],
    ]
    for time_of_day in times_of_day:
        start_time = time(time_of_day[0], time_of_day[1])
        new_availability = Availability.objects.create(date=today, start_time=start_time)
        new_availability.save()


class Migration(migrations.Migration):

    dependencies = [
        ("availabilities", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_availabilities_for_today),
    ]