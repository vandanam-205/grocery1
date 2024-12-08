from django.shortcuts import render,redirect
from django.http import HttpResponse
from groceryapp.models import *

def index(request):
    return render(request,'index.html')
def categorypage(request):
    data=category.objects.all()
    dic={'data':data}
    return render(request,'category.html',dic)
def contact(request):
    return render(request,'contact.html')
def about_us(request):
    return render(request,'index.html')
def productpage(request,pk):
    data=subcategory.objects.get(id=pk)
    subdata=product.objects.filter(categoryid=data)
    return render(request, 'product.html',{'subdata':subdata})


def subcategorypage(request,pk):
    data=category.objects.get(id=pk)
    subdata=subcategory.objects.filter(categoryid=data)
    return render(request, 'subcategorypage.html',{'subdata':subdata})

def userregister(request):
    message=''
    dic={}
    if request.method == 'POST':
        uname = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword=request.POST['cpassword']

        registerfilter=userregistration.objects.filter(username=uname,email=email,password=password)

        if registerfilter:
            message=' this account is exist please try another'
          
        else:
            if password == cpassword:
                insertdata=userregistration.objects.create(username=uname,email=email,password=password,cpassword=cpassword)
                message='register successful'
                # return redirect('login')
                return render(request,'login.html',{'msg':message})
            else:
                message='password does not match'
    dic={'msg':message}
    return render(request,'register.html',dic)

def login(request):
    message=''
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        f=userregistration.objects.filter(email=email,password=password).first()
        if f:
            sessiondata=request.session['username']=f.username
            return redirect('index2')
        else:
            message='first do registration'
    return render(request,'login.html',{'msg':message})

def index2(request):
    return render(request,'index-2.html')


