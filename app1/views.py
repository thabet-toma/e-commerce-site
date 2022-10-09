from django.shortcuts import render

# Create your views here.

def us(request):
    return render(request,'aboutus.html')