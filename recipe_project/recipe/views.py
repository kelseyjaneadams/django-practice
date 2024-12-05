from django.shortcuts import render, redirect
from .forms import RecipeForm
from .models import Recipe

# Create your views here.

# The add_recipe function handles the addition of a recipe. 
# If a POST request is received, a new form instance is created with the submitted data. 
# The form instance is then validated and saved to the database, 
# and then the user is redirected to a page that lists all the recipes
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_recipes')
    else:
        form = RecipeForm()
    return render(request, 'recipe/add_recipe.html', {'form': form})


# This function retrieves all the recipe records from the database using the `Recipe.objects.all()` query.
# It then passes the list of recipes to the 'list_recipes.html' template for rendering.
# The recipes are made available to the template via the context dictionary with the key 'recipes'.
def list_recipes(request):
    recipes = Recipe.objects.all() # retrieve all the recipes
    return render(request, 'recipe/list_recipes.html', {'recipes': recipes})
