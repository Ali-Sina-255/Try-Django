from typing import Iterable
from django.db import models
from django.conf import settings
from . validator import validate_unite_mesasure
from django.urls import reverse


class Recipes(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True,
                             on_delete=models.SET_NULL)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    directions = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
    
        return self.name

    
    def get_recipe_detail_urls(self):
        return reverse('recipe:detail', kwargs={"id": self.id})
    
    def get_hx_url(self):
        return reverse('recipe:hx-detail',kwargs={"id": self.id})

    def get_recipe_list_url(self):
        return reverse("recipe:recipe-list")
    
    def get_edite_url(self):
        return reverse('recipe:update', kwargs={"id": self.id})


    def delete_recipes(self):
        return reverse('recipe:delete', kwargs={"id": self.id})

    
class RecipeIngredient(models.Model):
    recipes = models.ForeignKey(
        Recipes, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    directions = models.TextField(null=True, blank=True)
    quantity = models.CharField(max_length=100)
    quantity_as_flout = models.FloatField(blank=True, null=True)
    unit = models.CharField(max_length=50, validators=[
                            validate_unite_mesasure])
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    avtive = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    