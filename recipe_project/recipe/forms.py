from django import forms
from .models import Recipe


# The RecipeForm class is a Django form that is based on the Recipe model. It inherits from ModelForm, 
# indicating that the form is tied to a specific model. The Meta class inside it specifies:
# model = Recipe: The form is linked to the Recipe model.
# fields = ['name', 'ingredients', 'instructions']: Only these fields from the Recipe model
#  will be included in the form.
# This allows you to create a form for creating or updating Recipe instances, with only the specified fields.
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'ingredients', 'instructions']

