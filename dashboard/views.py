from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth


# Create your views here.
@login_required
def dashboard(request):
    return render(request,"dashboard/dashboard.html")

