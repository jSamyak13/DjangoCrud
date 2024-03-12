from django.shortcuts import render, redirect
from .models import User

# Create your views here.

def index(request):
    return render(request, "home.html")

def signup(request):
    return render(request, "signup.html")

def insert(request):
    name = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    confirm = request.POST['confirmPassword']
    if password == confirm:
        us = User(username=name, email=email, password=password, confirm=confirm)
        us.save()
        return render(request, "home.html")

    return render(request, "signup.html", {"text":"password did not match"})

def login(request):
    email = request.POST['email']
    password = request.POST['password']

    email_exist = User.objects.filter(email=email).exists()
    password_exist = User.objects.filter(password=password).exists()


    if email_exist == True and password_exist == True:
        return show_data(request)
    elif email_exist == True and password_exist == False:
        return render(request, 'login.html', {'text':'Wrong Password'})
    else:
        return render(request, 'home.html', {'text':'You Need to Sign Up First'})


def login_user(request): 
    return render(request, "login.html")

def show_data(request): 
    users = User.objects.all()
    return render(request, "show_data.html", {"data":users})

def delete(request, id):
    field = User.objects.get(id = id)
    field.delete()
    return redirect("/data/")

def update(request, id):
    id = User.objects.get(id = id)
    print(id.id)
    return render(request, "update.html", {"id":id.id})

def edit(request, id):
    email = request.POST['email']
    password = request.POST['password']
    cnmf = request.POST['confirmPassword']
    User.objects.filter(id=id).update(email=email, password = password, confirm = cnmf)
    return redirect("/data/")