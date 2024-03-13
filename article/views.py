from django.shortcuts import render, redirect
from . models import Articles
from django.contrib import messages
from . forms import ArticlesFroms


def article_create_view(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('account:login')

    context = {}

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article_object = Articles.objects.create(title=title, content=content)
        context['object'] = article_object
        context['created'] = True

    return render(request, 'index.html', context=context)


def article_create_form(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('account:login')
    forms = ArticlesFroms(request.POST or None)
    context = {
        'forms': forms
    }
    if request.method == "POST":
        forms = ArticlesFroms(request.POST)
        if forms.is_valid():
            title = forms.cleaned_data.get('title')
            content = forms.cleaned_data.get('content')
            article_object = Articles.objects.create(
                title=title, content=content)
            context['object'] = article_object
        else:
            print(forms.error)
    return render(request, 'article_create.html', context=context)


def article_detail_view(request, value_from_url, *args, **kargs):
    articlce_detail = Articles.objects.get(id=value_from_url)

    context = {
        'articlce_detail': articlce_detail
    }
    return render(request, 'detail.html', context=context)


def all_article_list(request, *args, **Kwargs):
    articles = Articles.objects.all()
    context = {
        "articles": articles
    }
    return render(request, 'index.html', context)
