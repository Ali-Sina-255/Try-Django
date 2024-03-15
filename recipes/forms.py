from typing import Any
from django.forms import ModelForm
from . models import Recipes, RecipeIngredient


class RecipesForm(ModelForm):
    class Meta:
        model = Recipes
        fields = ["name", "description", "directions"]

    def clean(self):
        cleaned_data = self.cleaned_data
        print("all clean data")
        return cleaned_data


class RecipeIngredientForm(ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ["name", "unit", "quantity"]

    def clean(self):
        cleaned_data = self.cleaned_data
        print("all clean data")
        return cleaned_data
