from django import forms
from ingredients.models import Ingredient
from .models import ProductIngredient

class ProductForm(forms.Form):
    name = forms.CharField(max_length=250, required=True)
    description = forms.CharField(max_length=250)
    price = forms.FloatField(required=True)

class ProductIngredientForm(forms.ModelForm):
    ingredient = forms.ModelChoiceField(queryset=Ingredient.objects.all(), to_field_name = 'name', empty_label="Select Ingredient", required=True)

    class Meta:
        model = ProductIngredient
        fields = ('ingredient', 'qty')

