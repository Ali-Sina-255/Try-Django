from django.shortcuts import render, redirect
from . models import Articles
from django.contrib import messages
from . forms import ArticlesFroms
from django.http import Http404
from django.db.models import Q

def article_search_view(request, *args, **kwargs):
    query = request.GET.get("q")
    qs = Articles.objects.all()
    if query is not None:
        # lookups = Q(title__icontains=qery) | Q(content__icontains=qery)
        
        qs = Articles.objects.search(query)
    context = {
        'object_list': qs
    }
    return render(request, 'articles/search.html', context)


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

    return render(request, 'articles/index.html', context=context)


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
    return render(request, 'articles/article_create.html', context=context)


def article_detail_view(request, slug=None, *args, **kargs):
    articlce_detail = None
    if slug is not None:
        try:
            articlce_detail = Articles.objects.get(slug=slug)
        except Articles.DoesNotExist:
            raise Http404
        except Articles.MultipleObjectsReturned:
            articlce_detail = Articles.objects.get(slug=slug).first()
        except:
            raise Http404
    context = {
        'articlce_detail': articlce_detail
    }
    return render(request, 'articles/detail.html', context=context)


def all_article_list(request, *args, **Kwargs):
    articles = Articles.objects.all()
    context = {
        "articles": articles
    }
    return render(request, 'articles/index.html', context)
