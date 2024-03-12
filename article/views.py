from django.shortcuts import render
from . models import Articles
from django.contrib import messages


def article_create_view(request, *args, **kargs):

    context = {}
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article_object = Articles.objects.create(title=title, content=content)
        context['object'] = article_object
        context['created'] = True

    return render(request, 'index.html', context=context)


def article_detail_view(request, value_from_url, *args, **kargs):
    articlce_detail = Articles.objects.get(id=value_from_url)

    context = {
        'articlce_detail': articlce_detail
    }
    return render(request, 'detail.html', context=context)
