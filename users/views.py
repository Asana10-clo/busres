from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your views here.
def profile(request):
    return render(request,'profile.html')


def login(request):
    
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']

        user = authenticate(email=email, password = password)

        print(user)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')

def signup(request):
    if request.method =='POST':
       
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username has been taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                 messages.info(request,'Email Taken')
                 return redirect('signup')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password1,
                    email=email,
                    first_name=first_name,
                    last_name=last_name)
                user.save();
                print('User Created')
                return redirect('login')
            
        else:
                messages.info(request,'Password not matching')
                return redirect('signup')
            


    else:
       return render(request, 'sign up.html')