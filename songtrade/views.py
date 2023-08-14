from django.http import JsonResponse
from django.shortcuts import render,redirect
from .models import Songs
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,Group
from django.contrib import messages
from datetime import date, timedelta


# Create your views here.

def home(request):
    latest_song = Songs.objects.filter(recent_song__gt=date.today() + timedelta(days=-7))[:6]
    return render(request,"index.html",{"latest_song": latest_song})
 

def sign_in(request):
    try:
        if request.method == "POST":
            print(request.POST)
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
          
            if user is not None:
                login(request, user)
                messages.success(request,"successfully logged in")  
                return redirect("song-dashboard")
            else:
                messages.error(request,"incorrect user or password !")
                return redirect("login")
            
    except Exception as e:
        print("please enter valid user",e)
    return render (request,"login.html")
    

def artist_signup(request):
    try:

        if request.method == "POST":
    
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            user = User.objects.create_user(username=username, email=email, password=password)
            group =  Group.objects.get(name="artist")
            user.groups.add(group)
            
            messages.success(request,"you have successfully created Account")
            return redirect("artist_signup")
        
        elif request.method == "GET":
            return render(request,"artist_signup.html")
    
        return render(request,"artist_signup.html")
    except Exception:
          print("not created successfully!")


def investor_signup(request):
    try:

        if request.method == "POST":
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            user = User.objects.create_user(username=username, email=email, password=password)
            group =  Group.objects.get(name="investor")
            user.groups.add(group)
            messages.success(request,"you have successfully created Account")
            return redirect("signup")
        elif request.method == "GET":
            return render(request,"signup.html")
    
        return render(request,"signup.html")
    except Exception:
          print("not created successfully!")


def forgot_password(request):
    
    return render (request,"forgot-password.html")

def reset_password(request):
    return render(request, "reset-password.html")

def logout_user(request):
    logout(request)
    messages.success(request,"you have logged Out ")
    return redirect("login")


def song_dashboard(request):
    if request.user.is_authenticated:
       users = User.objects.all().exclude(is_superuser = True)[:5]
       recent_release = Songs.objects.filter(recent_song__gt=date.today() + timedelta(days=-7))[:4]
       return render(request,"song-dashboard.html",{"recent_release":recent_release,"users":users})
    else:
        messages.error(request, "please log in first !")
        return redirect("home")

        
def editions(request,slug):
    if request.user.is_authenticated:
         users = User.objects.all().exclude(is_superuser = True)[:10]
         songs = Songs.objects.get(slug=slug)
         return render(request,"editions.html",{"songs":songs,"users":users})
    else:
        messages.error(request," To view the page login first ")
        return redirect("home")

def checkout(request,slug):
    songs = Songs.objects.get(slug=slug)
    return render(request,"checkout.html",{"songs":songs})


def add_songs(request):
    try:
        if request.method == "POST":
            print("success")
            song_name = request.POST.get("song_name")
            song_price = request.POST.get("song_price")
            song_image = request.FILES.get("song_image")
            song_description = request.POST.get("song_description")
            Songs.objects.create(artist_name=request.user,song_name=song_name,song_price=song_price,song_image=song_image,slug=song_description)
            return redirect("song-list")   
            
    except Exception  as e:
        print(f"{e=}")
        return render(request,"song-dashboard") 
def edit_songs(request):
    return render(request,"index.html")
  

def song_list(request):
    print(request.user)
    try:
        fetch_song = Songs.objects.filter(artist_name=request.user)
        print(fetch_song)
        return render(request,'song-item.html',{"fetch_songs":fetch_song})
    except Exception as ep :
        print(f"{ep=}")
        return redirect("song-list")


def delete_song(reqeust,slug):
   
        song = Songs.objects.get(slug=slug)
        song.delete()
        return JsonResponse({'message': 'Song deleted successfully'}, status=200)



