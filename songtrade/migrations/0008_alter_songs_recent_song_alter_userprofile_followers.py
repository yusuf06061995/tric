# Generated by Django 4.2 on 2023-09-01 10:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songtrade', '0007_alter_songs_recent_song_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='recent_song',
            field=models.DateField(default=datetime.datetime(2023, 9, 1, 10, 6, 11, 874379)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='following', to='songtrade.userprofile'),
        ),
    ]
