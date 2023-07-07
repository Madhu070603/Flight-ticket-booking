# Generated by Django 4.1.7 on 2023-07-07 06:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=50)),
                ('time_start', models.CharField(max_length=50)),
                ('time_end', models.CharField(max_length=50)),
                ('room_number', models.CharField(max_length=50)),
                ('appointment_with', models.CharField(blank=True, max_length=50)),
                ('update_time', models.DateField(auto_now=True)),
                ('first_time', models.DateField(auto_now_add=True)),
                ('exam_name', models.CharField(max_length=100)),
                ('capacity', models.PositiveIntegerField(default=1)),
                ('booked_count', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
