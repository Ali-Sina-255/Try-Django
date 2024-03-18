from typing import Any
from . models import Recipes, RecipeIngredient
from django import forms


class RecipesForm(forms.ModelForm):
    required_css_class = 'required-filed'
    error_class = 'rerror-filed'
    name = forms.CharField(help_text="This is your help.<a href ='/contact'>Contact as </a>" )
    # description = forms.CharField(widget=forms.Textarea(attrs={"rows":6, "placeholder":"Recips Description"}))
    # directions = forms.CharField(widget=forms.Textarea(attrs={"rows":6, "placeholder":"Recips directions"}))
    
    class Meta:
        model = Recipes
        fields = ["name", "description", "directions"]

    def clean(self):
        cleaned_data = self.cleaned_data
        print("all clean data")
        return cleaned_data

    # anther way 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs.update({"class":"form-control2", 'placholder':'update from init fuction'})
        # self.fields['description'].widget.attrs.update({"class":"form-control2", 'placholder':'update from init fuction'})
        # self.fields['directions'].widget.attrs.update({"class":"form-control2", 'placholder':'update from init fuction'})
        for field in self.fields:
            context = {
                "placeholder":f"Recipe {str(field)}",
                "class": "form-control3"
            }
            self.fields[str(field)].widget.attrs.update(context)

class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ["name", "unit", "quantity"]

    def clean(self):
        cleaned_data = self.cleaned_data
        print("all clean data")
        return cleaned_data
