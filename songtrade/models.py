from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import datetime





class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField("self", related_name='following',symmetrical=False, blank=True)

    def __str__(self):
        return self.user.username
    










class Songs(models.Model):

    song_choice = [
        ("GOLD", "Gold"),
        ("DIAMOND", "Diamond"),
        ("SILVER","Silver")
    ]
    song_packages = models.CharField(max_length=10,choices=song_choice,default=song_choice[0][0])
    artist_name = models.ForeignKey(User, models.DO_NOTHING)
    song_name = models.CharField(max_length=100,unique=True)
    songs_description = models.CharField(max_length=100, blank=True)
    song_image = models.ImageField(upload_to="song-media",unique=True)
    song_price = models.IntegerField(default=0)
    recent_song  = models.DateField(default=datetime.datetime.now())
    slug = models.SlugField(default="artist-name")


    def save(self, *args, **kwargs):
        self.slug = slugify(self.song_name)
        super(Songs, self).save(*args, **kwargs)

    # def create(self, *args, **kwargs):
    #     self.slug = slugify(self.songs_description)
    #     super(Songs, self).create(*args, **kwargs)


    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Songs'
        verbose_name_plural = 'Songs'



    def __str__(self):
        return self.song_name

