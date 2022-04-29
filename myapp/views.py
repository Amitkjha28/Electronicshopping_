from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def myindex(request):
    return render(request,'index.html')

def mylogin(request):
    return render(request,'login.html')

def mysignup(request):
    return render(request,'signup.html')

# def mycomputer(request):
#     return render(request,'computer.html')
#
# def mylaptop(request):
#     return render(request,'laptop.html')
#
# def myproduct(request):
#     return render(request,'product.html')
#
# def mycontact(request):
#     return render(request,'contact.html')

