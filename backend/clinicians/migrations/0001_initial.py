# Generated by Django 3.0 on 2021-04-21 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('availabilities', '0002_auto_20200418_1807'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('available', 'Available'), ('booked', 'Booked')], max_length=10)),
                ('availability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='availabilities.Availability')),
            ],
        ),
        migrations.CreateModel(
            name='Clinician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('national_provider_identifier', models.CharField(max_length=10, unique=True)),
                ('availabilities', models.ManyToManyField(through='clinicians.Appointment', to='availabilities.Availability')),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='clinician',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinicians.Clinician'),
        ),
    ]
