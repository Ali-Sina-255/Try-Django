from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from requests import delete
from . models import Recipes
from . forms import RecipesForm


@login_required
def recipe_list_view(request):
    all_recipes = Recipes.objects.filter(user=request.user)
    context = {
        'all_recipes': all_recipes
    }
    return render(request, 'recipes/recipe_list.html', context)


@login_required
def recipe_detail_view(request, value_from_url=None):
    query_set = get_object_or_404(
        Recipes, id=value_from_url, user=request.user)
    context = {
        'query_set': query_set
    }
    return render(request, 'recipes/recipe_detail.html', context)


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
        return redirect(obj.get_recipe_list_url())
    return render(request, 'recipes/recipe_create.html', context)


# Node for update we need to create form
@login_required
def recipe_update_views(request, value_from_url):
    object = get_object_or_404(
        Recipes, id=value_from_url, user=request.user)
    
    form = RecipesForm(request.POST or None, instance=object)
    context = {
        "object": object,
        'form': form
    }
    if request.method == "POST":
        form = RecipesForm(request.POST, instance=object)
        if form.is_valid():
            form.save()
            context["message"] = "Data Saved"
            return redirect(object.get_recipe_list_url())
        else:
            print(form.errors)
            form = RecipesForm()
    
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
