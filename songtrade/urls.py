from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('login/',sign_in,name="login"),
    path('artist-signup/',artist_signup,name="artist-signup"),
    path('signup/',investor_signup,name="signup"),
    path('forgot-password/',forgot_password,name="forgot-password"),
    path('reset-password/',reset_password,name="reset-password"),
    path('logout/',logout_user,name="logout"),
    path('song-dashboard/',song_dashboard,name="song-dashboard"),
    path('editions/<slug:slug>',editions,name='editions'),
    path('checkout/<slug:slug>',checkout,name='checkout'),
    path('add-songs',add_songs,name='add-songs'),
    path('delete-song/<slug:slug>',delete_song,name='delete-song'),
    path('song-list/',song_list,name='song-list'),
    path('profile/<int:slug>',user_profile,name='profile'),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)