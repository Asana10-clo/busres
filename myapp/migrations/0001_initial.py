# Generated by Django 4.1.1 on 2022-10-03 10:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import geolocation_fields.models.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('lastModified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('short_name', models.CharField(max_length=10, unique=True)),
                ('phone', models.CharField(blank=True, max_length=17, null=True, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('address', models.CharField(blank=True, max_length=90, null=True, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('website', models.URLField(blank=True, null=True, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('lastModified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=60, unique=True)),
                ('point', geolocation_fields.models.fields.PointField(unique=True, verbose_name='point')),
                ('town', models.CharField(blank=True, max_length=60, null=True)),
                ('city', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('lastModified', models.DateTimeField(auto_now=True)),
                ('duration', models.DurationField(blank=True, null=True)),
                ('departure_point', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='routes_departure', to='myapp.point')),
                ('destination_point', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='routes_destination', to='myapp.point')),
            ],
            options={
                'unique_together': {('departure_point', 'destination_point')},
            },
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('lastModified', models.DateTimeField(auto_now=True)),
                ('fare', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField(blank=True, null=True)),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='myapp.operator')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='myapp.route')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TripSchedule',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('lastModified', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='myapp.trip')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TakeOff',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('lastModified', models.DateTimeField(auto_now=True)),
                ('time', models.TimeField()),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='take_offs', to='myapp.trip')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
