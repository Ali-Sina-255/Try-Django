from django.contrib import admin
from . models import RecipeIngredient, Recipes
from django.contrib.auth import get_user_model

User = get_user_model()

class RecipesInline(admin.TabularInline):
    model = Recipes
    extra = 0
    
    
class UserAdmin(admin.ModelAdmin):
    inlines = [RecipesInline]
    list_display =  ['username']
   
 
class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    fields = ['name', 'quantity', 'unit', 'directions']
    extra = 0

class RecipesAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display = ['id','user','name', 'active']
    list_display_links = ['id', 'user', 'name']
    readonly_fields = ['timestamp', 'update']   
    raw_id_fields = ['user']
admin.site.register(Recipes, RecipesAdmin)