from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def login_view(request, *args, **Kwargs):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            context = {
                "error": 'Invalid username or passowrd'
            }
            return render(request, 'account/login.html', context)

        login(request, user)
        messages.success(request, 'you are login new')
        return redirect('/')

    return render(request, 'account/login.html', {})


def user_registration_form(request):
    forms = UserCreationForm(request.POST or None)
    if forms.is_valid():
        forms.save()
        return redirect('account:login')
    context = {
        'forms': forms

    }
    return render(request, 'account/register.html', context)


def login_authentication_form(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm(request)
    context = { 
        "form": form
    }
    return render(request, 'account/login.html', context)
