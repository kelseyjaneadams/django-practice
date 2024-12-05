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


# This function retrieves a specific recipe from the database using the `recipe_id` parameter.
# If the request method is POST, it validates the submitted form data and updates the recipe in the database.
# If the request method is not POST, it pre-fills the form with the current recipe data and renders the update form.
# Once the form is successfully submitted, the user is redirected to the recipe list page ('list_recipes').
def update_recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('list_recipes')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipe/update_recipe.html', {'form': form})
