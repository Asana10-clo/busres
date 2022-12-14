# Generated by Django 4.1.3 on 2022-11-02 22:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('lastModified', models.DateTimeField(auto_now=True)),
                ('seat_no', models.PositiveIntegerField(blank=True, null=True)),
                ('trip_id', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
