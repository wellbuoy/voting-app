from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

def index(request):

    # Render the index.html page
    return render(request, 'page/index.html')

#Handles login functionality.
def login_view(request):
    if request.method == 'POST':

        # Check if form data is valid
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():

             # Get the valid user
            user = form.get_user()

            # Log in the user
            login(request, user)

            # Redirect to index page
            return redirect('index')
        
    else:

        # Create an empty form for GET requests
        form = AuthenticationForm()

    # Render the login page with the form
    return render(request, 'page/login.html', {'form': form})


# Handles user registration process
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        # Form data submission.
        if form.is_valid():

            # Valid form data, save and log in user.
            user = form.save()
            login(request, user)
            return redirect('login')
    else:

        # Render form for user registration
        form = UserCreationForm()
    return render(request, 'page/register.html', {'form': form})