from django.shortcuts import render, redirect
from .forms import RegisterationForm, LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def RegisterView(request):
    if request.method == 'POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], cd['password'])
            messages.success(request, 'you registrated successfully', 'success')
            return redirect('home')
    else:
        form = RegisterationForm()
    return render(request, 'register.html', {'form': form})



def LoginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username= cd['username'], password= cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'you logged in successfully', 'success')
                return redirect('home')
            else:
                messages.error(request, 'username or password is wrong', 'danger')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
    


def LogoutView(request):
    logout(request)
    messages.success(request, 'you logged out successfully', 'success')
    return redirect('home')