from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method == "POST":
        get_name=request.POST.get('username')
        get_email=request.POST.get('email')
        get_pass1=request.POST.get('pass1')
        get_pass2=request.POST.get('pass2')
        
        
        if get_pass1 != get_pass2:
            messages.info(request,"password is not matching!")
            return redirect("/auth/signup")
        try:
            if User.objects.get(username=get_name):
                messages.warning(request,"Username already exist")
                return redirect("/auth/signup")
            elif User.objects.get(email=get_email):
                messages.warning(request,"Email already exist")
                return redirect("/auth/signup")
                
        except Exception as indentifier:
            pass
        myuser=User.objects.create_user(get_name,get_email,get_pass1)
        myuser.save()
        messages.success(request,"User created successfully")
        return redirect("/auth/login")
        
        
    return render(request,'signup.html')

def handlelogin(request):
    if request.method=="POST":
        get_name=request.POST.get('username')
        get_pass1=request.POST.get('pass1')
        myuser=authenticate(username=get_name,password=get_pass1)
        
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login successfully")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")
        
    return render(request,'login.html')

def handlelogout(request):
    logout(request)
    messages.success(request,"logout successfully")
    return render(request,'login.html')