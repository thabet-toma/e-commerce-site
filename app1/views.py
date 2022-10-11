from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return redirect('/home')
def home1(request):
    return render(request,'home.html')
def reg(request):
    return render(request,'reg.html')
def pc(request):
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
