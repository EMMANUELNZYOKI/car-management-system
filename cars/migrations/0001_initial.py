# Generated by Django 5.0.2 on 2024-09-02 08:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year', models.PositiveIntegerField()),
                ('mileage', models.PositiveIntegerField()),
                ('color', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car')),
            ],
        ),
        migrations.CreateModel(
            name='DropOff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drop_off_time', models.DateTimeField(auto_now_add=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.vehiclelocation')),
            ],
        ),
    ]
