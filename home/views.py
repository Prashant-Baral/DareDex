from django.shortcuts import render, redirect
from . models import Dareupload, Contact


def home(request):
    return render(request,"home.html")


def about(request):
    return render(request,"about.html")


def contact(request):
    return render(request,"contact.html")




def display(request):
    contacts = Contact.objects.all()
    paramters ={
        'contacts' : contacts,
    }
    return render(request,"display.html",paramters)





def dcontact(request):
    if request.method=="POST":
        print("post recieved")
        user_name = request.POST.get("name")
        user_email = request.POST.get("email")
        user_message = request.POST.get("message")

        new_dcontact = Contact.objects.create(
            name=user_name,
            email=user_email,
            message=user_message
        )
        return redirect("contact")
        
    return render(request,"contact.html")





# DashBoard 
def dashboard(request):
    dares = Dareupload.objects.all().order_by("-id")
    
    parameters = {
        'dares': dares,
    }
    return render(request, 'dashboard.html', parameters)





#  Dares Page 
def dare(request):
    return render(request,"dare.html")


 # Creating Dare 
def create_dares(request):
    if request.method =="POST":
        print(" POST request received")
        user_name = request.POST.get("name")
        user_title = request.POST.get("title")
        user_category= request.POST.get("category")
        user_dare = request.POST.get("dare")
        user_level = request.POST.get("level")
        user_duration = request.POST.get("duration")
        user_safety = request.POST.get("safety")
        
        new_dare = Dareupload.objects.create(
            name=user_name,
            title=user_title,
            category=user_category,
            dare = user_dare,
            level=user_level,
            duration=user_duration,
            safety=user_safety
        )
        new_dare.save()
        
        return redirect('/dashboard/?submitted=1')
    
    return render(request,"dare.html")



# deleting dare

def delete_dare(request,id):
    dare = Dareupload.objects.get(id=id)
    dare.delete()
    return redirect('dashboard')


# edit dare
def edit_dare(request,id):

    dare = Dareupload.objects.get(id=id)

    if request.method =="POST":
        print(" POST request received")
        user_name = request.POST.get("name")
        user_title = request.POST.get("title")
        user_category= request.POST.get("category")
        user_dare = request.POST.get("dare")
        user_level = request.POST.get("level")
        user_duration = request.POST.get("duration")
        user_safety = request.POST.get("safety")
        
      
        dare.name = user_name
        dare.title = user_title
        dare.category = user_category
        dare.dare = user_dare
        dare.level = user_level
        dare.duration = user_duration
        dare.safety = user_safety
        dare.save()
        
        return redirect('dashboard')

    parameters = {
        "dare" : dare
    }
    return render(request,"edit_dare.html",parameters)