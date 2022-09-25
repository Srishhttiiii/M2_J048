import email
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contactus, Specialskills
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.admin import User
from django.contrib.auth.decorators import login_required,permission_required

# Create your views here.
def home(request):
    return render(request, 'index.html')


@login_required(login_url='login')
def services(request):
    try:
        data = Specialskills.objects.all()
        context = {"special":data}
    except Exception as e:
        context = {"special": "Not found"}
    return render(request, 'services.html', context)

def more(request,pk):
    fetchdata = Specialskills.objects.get(name=pk)
    print(fetchdata)
    context = {'fetchdata': fetchdata}
    return render(request, 'more.html', context)

@login_required(login_url='login')
def add(request):
    if request.method == 'POST':
        proj = Specialskills()
        proj.name = request.POST['name']
        proj.description = request.POST['description']
        proj.Day = request.POST['Day']
        proj.Assignment = request.POST['Assignment']
        proj.Journaling = request.POST['Journaling']
        proj.Cycling = request.POST['Cycling']
        proj.Workout = request.POST['Workout']
        proj.Grooming = request.POST['Grooming']
        proj.save()

    return render(request, 'add.html')

@login_required(login_url='login')
def delete(request,id):
    data = Specialskills.objects.get(id=id)
    data.delete()
    return redirect('services')

@login_required(login_url='login')
def update(request,id):
    if request.method == 'POST':
        new_name = request.POST['new_name']
        new_description = request.POST['new_description']
        new_assignment = request.POST['new_assignment']
        new_journaling = request.POST['new_journaling']
        new_cycling = request.POST['new_cycling']
        new_grooming = request.POST['new_grooming']
        new_workout = request.POST['new_workout']
        new_day = request.POST['new_day']
        data = Specialskills.objects.get(id=id)
        data.name = new_name
        data.description = new_description
        data.Assignment = new_assignment
        data.Journaling = new_journaling
        data.Cycling = new_cycling
        data.Grooming = new_grooming
        data.Workout = new_workout
        data.Day = new_day
        data.save()
        context = {'data':data}
        return redirect('services')

    context = {"data": "Not found"}
    return render(request, 'update.html', context)


def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    if request.method == 'POST':
        cu = Contactus()
        cu.name = request.POST['name']
        cu.phone = request.POST['phone']
        cu.context = request.POST['context']
        cu.save()

    return render(request, 'contactus.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    user=User.objects.create_user(username = username, email = email, password=password)
                    user.save()
                    print("New User Created")
                    login(request, user)
        return redirect('home')
    return render(request,'signup.html')

def Logout(request):
    logout(request)
    return redirect('home')
