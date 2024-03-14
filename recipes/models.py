from django.db import models
from django.conf import settings


class Recipes(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True,
                             on_delete=models.SET_NULL)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    directions = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    avtive = models.BooleanField(default=True)


class RecipeIngredient(models.Model):
    recipes = models.ForeignKey(Recipes, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    directions = models.TextField(null=True, blank=True)
    quantity = models.CharField(max_length=100)
    unit = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    avtive = models.BooleanField(default=True)
