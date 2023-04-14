from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
# Create your views here.

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        
        newUser = User(username = username)
        newUser.set_password(password)
        newUser.save()
        
        login(request, newUser)
        messages.success(request, "Successfully register")
        return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def loginUser(request):
    form = LoginForm(request.POST or None)
    
    context = {
        'form': form
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        
        user = authenticate(username = username, password = password)
        
        if user is None:
            messages.info(request,"Name or Password incorrect!!!")
            return render(request,'login.html',context)
        
        messages.success(request,"Successfully Login")
        login(request, user)
        return redirect('home')
    return render(request,'login.html',context)
    
    
def logoutUser(request):
    logout(request)
    messages.success(request,"Successfully Logout")
    return redirect('home')