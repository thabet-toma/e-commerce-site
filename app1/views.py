from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return redirect('/home')
def home1(request):
    return render(request,'home.html')
def reg(request):
    return render(request,'reg.html')
