from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
import  bcrypt

# Create your views here.
def home(request):
    return redirect('/home')
def home1(request):
    return render(request,'home.html')
def reg(request):
    return render(request,'reg.html')
def pc(request):
    context={
        'allproduct':products.objects.all()
    }
    return render(request,'pc.html')
def login(request):
    
    return render(request,'login.html')
def phones(request):
    return render(request,'phones.html')
def electronicTool(request):
    return render(request,'electronicTool.html')
def pro123(request):
    
    return render(request,'admin.html')
def show(request):
    return render(request,'showproduct.html')
def regProc(request):
    
    hash=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    x=location.objects.create(city=request.POST['city'],region=request.POST('region'),street=request.POST('street'),building=request.POST('building'),apartment=request.POST('apartment'))
    Users.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password=hash,phone_number=request.POST['phone_number'],location=x)
    return redirect('home1.html')


def addproduct(request):
    errors = products.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/pro123')
    else:
        products.objects.create(name=request.POST['name'],
        model_y=request.POST['model'],
        description=request.POST['desc'],
        price=request.POST['prisce'],
        categotry=request.POST['catagory'],
        # image=request.FILES['upload']
        )
        return redirect('/admin')

    
