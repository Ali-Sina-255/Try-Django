from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


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
