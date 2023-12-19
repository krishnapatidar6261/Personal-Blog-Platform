from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def index(request):
    blogs=Blog.objects.all()

    return render(request,'index.html',{'blogs':blogs})


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
def login(request):
    
    if request.method=="POST":
        try:
            user=User.objects.get(email=request.POST['email'])
            if user.pwd==request.POST['password']:
                request.session['email']=user.email
                return render(request,'blogerIndex.html')
            else:
                msg="Incorrect Password"
                return render(request,'login.html',{'msg':msg})           
        except:
            msg="Email Not Register"
            return render(request,'login.html',{'msg':msg})
    else:
        return render(request,'login.html')

def blogerIndex(request):
    if request.method=="POST":
        user=User.objects.get(email=request.session['email'])
        Blog.objects.create(
            user=user,
            title=request.POST['title'],
            desc=request.POST['desc'],
        )
        return redirect('index')
            
    else:
        return render(request,'blogerIndex.html')

def logout(request):
    try:
        del request.session['email']
        return redirect('index')
    except:
        return redirect('index')

def detailView(request,pk):
    blogs=Blog.objects.get(pk=pk)
    return render(request,'detailView.html',{'blogs':blogs})
