from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    return render(request,'index.html')


def register(request):
    if request.method=="POST":
        try:
            User.objects.get(email=request.POST['email'])
            msg="Email Already Register"
            return render(request,'register.html',{'msg':msg})
        except:
            if request.POST['password']==request.POST['cpassword']:
                User.objects.create(
                    email=request.POST['email'],
                    fname=request.POST['fname'],
                    lname=request.POST['lastname'],
                    gender=request.POST['gender'],
                    addr=request.POST['address'],
                    pwd=request.POST['password'],
                )
                msg="Register Successfully"
                return render(request,'register.html',{'msg':msg})
            else:
                msg="Password and Confirm Password Does Not Matched"
                return render(request,'register.html',{'msg':msg})

    else:
        
        return render(request,'register.html')