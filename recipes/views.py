from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from requests import delete
from . models import Recipes, RecipeIngredient
from . forms import RecipesForm, RecipeIngredientForm
from django.forms.models import modelformset_factory
from django.http import HttpResponse
from django.urls import reverse


@login_required
def recipe_list_view(request):
    all_recipes = Recipes.objects.filter(
        user=request.user).order_by('-timestamp')
    context = {
        'all_recipes': all_recipes
    }
    return render(request, 'recipes/recipe_list.html', context)


@login_required
def recipe_detail_view(request, value_from_url=None):
    hx_url = reverse('recipe:hx-detail', kwargs={"id": value_from_url})
    context = {
        'hx_url': hx_url
    }
    return render(request, 'recipes/recipe_detail.html', context)


@login_required
def recipe_detail_hx_view(request, value_from_url=None):
    try:
        query_set = Recipes.objects.get(id=value_from_url, user=request.user)
    except:
        query_set = None

    if query_set is None:
        return HttpResponse('not Found')
    context = {
        'query_set': query_set
    }
    return render(request, 'partials/detail.html', context)


@login_required
def recipe_create_view(request):
    forms = RecipesForm(request.POST or None)
    context = {
        'forms': forms
    }
    if forms.is_valid():
        obj = forms.save(commit=False)
        obj.user = request.user
        obj.save()
    if request.htmx:
        return render(request, 'partials/create.html')
    return render(request, 'recipes/recipe_create.html', context)


# Note for update we need to create form
@login_required
def recipe_update_views(request, value_from_url):
    object = get_object_or_404(
        Recipes, id=value_from_url, user=request.user)

    form = RecipesForm(request.POST or None, instance=object)

    RecipeIngredientFormSet = modelformset_factory(
        RecipeIngredient, form=RecipeIngredientForm, extra=0)
    qs = object.recipeingredient_set.all()
    formset = RecipeIngredientFormSet(request.POST or None, queryset=qs)

    context = {
        "object": object,
        'form': form,
        "formset": formset
    }
    if request.method == "POST":
        form = RecipesForm(request.POST, instance=object)
        if all([form.is_valid(), formset.is_valid()]):
            parent = form.save(commit=False)
            parent.save()
            # formset.save()
            for form in formset:
                child = form.save(commit=False)
                if child.recipes is None:
                    print('Added new')
                    child.recipes = parent
                child.save()
            context["message"] = "Data Saved"
            
    if request.htmx:
        return render(request, 'partials/forms.html', context)
    return render(request, 'recipes/recipe_update.html', context)


@login_required
def recipe_delete_view(request, value_from_url):
    delete_recipes = get_object_or_404(
        Recipes, id=value_from_url, user=request.user)
    if request.method == 'POST':
        delete_recipes.delete()
        return redirect('recipe:recipe-list')
    context = {
        "delete_recipes": delete_recipes
    }
    return render(request, 'recipes/recipe_delete.html', context)
