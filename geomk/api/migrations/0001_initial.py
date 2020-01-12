# Generated by Django 3.0.2 on 2020-01-12 21:21

import api.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('left_time', models.DateTimeField(default='2020-01-01T00:00:00.000000Z')),
                ('time', models.CharField(default='0 minutes', max_length=13)),
                ('paid', models.BooleanField(default=False)),
                ('left', models.BooleanField(default=False)),
                ('plate', models.CharField(max_length=8, validators=[api.models.validate_plate])),
            ],
        ),
    ]
