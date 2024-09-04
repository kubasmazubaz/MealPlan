from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm, LoginForm  # Update import to match form name
from .models import UsersLogin

def registration_login(request):
    signup_form = SignUpForm()  # Use SignUpForm instead of RegisterForm
    login_form = LoginForm()

    if request.method == 'POST':
        if 'register' in request.POST:
            signup_form = SignUpForm(request.POST)  # Use SignUpForm instead of RegisterForm
            if signup_form.is_valid():
                user = signup_form.save()  # Save the user to the database
                # Create a UsersLogin record with the registered user
                UsersLogin.objects.create(
                    user=user,
                    email=user.email
                )
                return redirect('login')  # Redirect to a login page after registration
        elif 'login' in request.POST:
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('index')  # Redirect to a home page after login

    context = {
        'signup_form': signup_form,
        'login_form': login_form
    }
    return render(request, 'Users/registration_login.html', context)

def index(request):
    return render(request, 'Users/index.html')
