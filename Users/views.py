from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm, LoginForm
from .models import UsersLogin

def registration_login(request):
    signup_form = SignUpForm()
    login_form = LoginForm()

    if request.method == 'POST':
        if 'register' in request.POST:
            print("Registration form submitted")  # Step 1

            signup_form = SignUpForm(request.POST)
            if signup_form.is_valid():
                print("Registration form is valid")  # Step 2

                user = signup_form.save()  # Save the user to the database
                print(f"User created: {user}")  # Step 3

                # Create a UsersLogin record with the registered user
                users_login_record = UsersLogin.objects.create(
                    user=user,
                    email=user.email
                )
                print(f"UsersLogin record created: {users_login_record}")  # Step 4

                return redirect('login')  # Redirect to a login page after registration
            else:
                print(f"Form errors: {signup_form.errors}")  # Step 5

        elif 'login' in request.POST:
            print("Login form submitted")  # Step 6

            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                print("Login form is valid")  # Step 7

                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    print(f"User authenticated: {user}")  # Step 8
                    login(request, user)
                    return redirect('index')  # Redirect to a home page after login
                else:
                    print("Authentication failed")  # Step 9
            else:
                print(f"Login form errors: {login_form.errors}")  # Step 10

    # Render the page with both forms
    context = {
        'signup_form': signup_form,
        'login_form': login_form
    }
    return render(request, 'Users/registration_login.html', context)

def index(request):
    print("Index page accessed")  # For testing index view
    return render(request, 'Users/index.html')
