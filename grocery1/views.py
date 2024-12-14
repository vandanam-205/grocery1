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
def addcart(request):
    data=cartdata.objects.all()

    return render(request,'cart.html',{'data':data})
def cartdata1(request, pk):
    userdata = request.session.get('username', None)
    fdata = userregistration.objects.get(username=userdata) 
    data1 = product.objects.get(id=pk)
    productid = data1
    insertdata = cartdata.objects.create(
        user=fdata, 
        product=productid,
        productname=data1.productname,
        productimage=data1.productimage,
        productprice=data1.productprice
    )
    return redirect('addcart')

    
def productpage(request,pk):
    data=subcategory.objects.get(id=pk)
    subdata=product.objects.filter(categoryid=data)
    return render(request, 'product.html',{'subdata':subdata})

def productdetail(request,pk):
   
    data1=product.objects.get(id=pk)
    data=product_unit.objects.filter(product=data1)
   
    return render(request, 'productdetailpage.html',{'data':data,'data1':data1})


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


