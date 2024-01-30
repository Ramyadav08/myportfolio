from django.shortcuts import render
from django.shortcuts import render,redirect
from portfolioapp.models import Contact,Blogs
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    if request.method=="POST":
        get_name=request.POST.get('name')
        get_email=request.POST.get('email')
        get_phone=request.POST.get('phone')
        get_dis=request.POST.get('discription')
        
        query=Contact(name=get_name,email=get_email,phonenumber=get_phone,description=get_dis)
        query.save()
        messages.success(request,"we will get back you soon")
        
        return redirect('/contact')
        
    return render(request,"contact.html")

def handleblogs(request):
    posts=Blogs.objects.all()
    context={
        "posts":posts
    }
    return render(request,'handleblogs.html',context)
