# Generated by Django 4.2 on 2023-08-23 12:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songtrade', '0004_alter_songs_recent_song_alter_songs_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='recent_song',
            field=models.DateField(default=datetime.datetime(2023, 8, 23, 12, 0, 39, 772391)),
        ),
        migrations.AlterField(
            model_name='songs',
            name='songs_description',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
