from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.core import mail



# Create your views here.

def display(request):
    return render(request,'index.html')

def indexpage(request):
  return render(request,'index.html')

def view_mynotes(request):
   
    user = User.objects.get(id=request.user.id)
    notes = Notes.objects.filter(user = user)

    d = {'notes':notes}
    return render(request,'view_mynotes.html',d)

def signup2(request):
    error=""
    if request.method=='POST':
       uname = request.POST.get('name') 
       cont = request.POST.get('contact')
       email = request.POST.get('emailid')
       passc = request.POST.get('password')
       br1 = request.POST.get('branch')
       data ={
           uname,cont,email,passc,br1
       }
       try:
          if data is not None:
             my_user = User.objects.create_user(uname,email,passc)
             Signup.objects.create(user=my_user,email=email,contact=cont,branch=br1)
             my_user.save()
             error="no"
          else:
             error="yes"
       except:
             error="yes"
   
    return render(request,'signup.html',locals())
def loginpage(request):
    error=""
    if request.method=="POST":
        uname = request.POST.get('name')
        passc = request.POST.get('pass')

        user = authenticate(request,username=uname,password=passc)
        if user is not None:
            login(request,user)
            error="no"
            
        else:
            error="yes"
         
    return render(request,'login.html',locals())
       
def profilepage(request): 
    user = User.objects.get(id=request.user.id)
    signup1 = Signup.objects.filter(user = user)
    d = {'signup':signup1}
    
    return render(request,'profile.html',d)


    
def contactpage(request):
    if request.method == 'POST':
       usname = request.POST['name']
       mailid = request.POST['mailbox']
       phone = request.POST['phonenumber']
       message = request.POST['message']

       email = EmailMessage(
           subject='Contact enquiry',
           body = 'This mail is from: ' +mailid,
           from_email = mailid,
           to =
           ['omprakashvenkatesh11@gmail.com'],
       )
       email.send()
    
        
    return render(request,'contact.html',locals())  
       

      
       

def aboutpage(request):
    return render(request,'about.html')

def redirectpage(request):
  return render(request,'redirect.html')