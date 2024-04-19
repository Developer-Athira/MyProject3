from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from emplyapp.models import Emply
from django.db.models import Q
from django.contrib import messages

# Create your views here.

def user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        empID1=request.POST.get('empID')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        

        if password==confirmpassword:

            if User.objects.filter(username=username).exists():
                return redirect("http://127.0.0.1:8000/register/")
            elif User.objects.filter(email=email).exists():
                return redirect("http://127.0.0.1:8000/register/")
            elif Emply.objects.filter(Q(empId = empID1) & Q(email=email)):
                user_reg=User.objects.create_user(username=username,email=email,password=password)
                user_reg.save()
                return redirect("/")
            else:
                messages.error(request, 'Invalid email or Employee ID. Please try again.')
            
    return render(request,'user.html')


def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            return redirect("http://127.0.0.1:8000/register/")

    

    return render(request,'log.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def forgotpassword(request):
    return render(request,"forgotpassword.html")

# def resetpassword(request):
#     if request.method=='POST':
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         confirmpassword=request.POST.get('confirmpassword')

#         if password==confirmpassword:
