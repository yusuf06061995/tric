from django.db import models
from django.contrib.auth.models import User
import datetime



class Profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   uuser_image = models.ImageField(default='',  
                                     upload_to='song-media')
   def __str__(self):
      return self.user.username


# class CustomUser(User):
#     image = models.ImageField()

class Songs(models.Model):
    artist_name = models.ForeignKey(User, models.DO_NOTHING)
    song_name = models.CharField(max_length=100,unique=True)
    songs_description = models.CharField(max_length=100
                                         )
    song_image = models.ImageField(upload_to="song-media",unique=True)
    song_price = models.IntegerField(default=0)
    recent_song  = models.DateField(default=datetime.datetime.now())
    slug = models.SlugField(default="", null=False)
    


    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Songs'
        verbose_name_plural = 'Songs'



    def __str__(self):
        return self.song_name

