from django.shortcuts import render


def article_create_view(request, *args, **kargs):
    return render(request, 'index.html')