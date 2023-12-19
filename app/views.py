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
        return redirect('blogerIndex')
            
    else:
        return render(request,'blogerIndex.html')

def logout(request):
    try:
        del request.session['email']
        return redirect('index')
    except:
        return redirect('index')

def detailView(request,pk):
    try:
        blogs=Blog.objects.get(pk=pk)
        return render(request,'detailView.html',{'blogs':blogs})
    except:
        return render(request,'404.html')

def allUser(request):
    user=User.objects.all()
    return render(request,'allUser.html',{'user':user})

def update(request,pk):
    try:
        user=User.objects.get(pk=pk)
        if request.method=="POST":
            user.email=request.POST['email']
            user.fname=request.POST['fname']
            user.lname=request.POST['lastname']
            user.gender=request.POST['gender']
            user.addr=request.POST['address']

            user.save()
            return redirect('allUser')
        else:
            return render(request,'update.html',{'user':user})
    except:
        return render(request,'404.html')
def delete(request,pk):
    try:
        user=User.objects.get(pk=pk)
        user.delete()
        return redirect('allUser')
    except:
        return render(request,'404.html')