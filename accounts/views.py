from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Student
from django.contrib import messages

def register(request):
    
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        new_user = User.objects.create(
            username = username,
            first_name = first_name,
            last_name = last_name ,
            email = email,

        )

        new_user.set_password(password) #Setting the password for the new user in the encrypted format

        new_user.save()

        return redirect("home")

    return render(request,"accounts/register.html")


# Login
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        if Student.objects.filter(username=username).exists():
            user = auth.authenticate(request,username=username,password=password)


            if user is not None:
                auth.login(request,user) # this is the function to login
                return redirect("home")
            messages.error(request,"Invalid Username or Password")

    return render(request,"accounts/login.html")