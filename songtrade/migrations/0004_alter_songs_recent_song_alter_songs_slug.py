# Generated by Django 4.2 on 2023-08-23 11:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songtrade', '0003_alter_songs_recent_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='recent_song',
            field=models.DateField(default=datetime.datetime(2023, 8, 23, 11, 26, 32, 528783)),
        ),
        migrations.AlterField(
            model_name='songs',
            name='slug',
            field=models.SlugField(default='artist-name'),
        ),
    ]
