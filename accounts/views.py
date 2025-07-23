from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Student
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        new_user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = email
        )
        new_user.set_password(password)  # stting the password for the new user in encrypted format.(hashsed format)
        new_user.save()
        return redirect("home")
    
    
    
    return render(request,"accounts/register.html")


# Login

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(request, username = username , password = password)

        if user is not None :
            auth.login(request,user)
            return redirect("dashboard")
        
        messages.error(request,"Invalid username or password")

    return render(request,"accounts/login.html")

# Log out
@login_required
def logout(request):
    auth.logout(request)
    return redirect("home")