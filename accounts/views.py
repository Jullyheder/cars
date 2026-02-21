from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

# Create your views here.
def register_view(request):
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('login_view')
    
    return render(request, 'register.html', {'form': form})


def login_view(request):
    form = AuthenticationForm()
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(
            request,
            username=username,
            password=password
        )
        
        if user is not None:
            login(request, user)
            return redirect('cars_view')

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('cars_view')