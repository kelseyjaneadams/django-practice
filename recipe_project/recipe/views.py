from django.db import IntegrityError
from django.shortcuts import render, redirect
from .forms import RecipeForm
from .models import Recipe
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.


# The add_recipe function handles the addition of a recipe. 
# If a POST request is received, a new form instance is created with the submitted data. 
# The form instance is then validated and saved to the database, 
# and then the user is redirected to a page that lists all the recipes
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            try:
                # Check if a recipe with the same name already exists
                name = form.cleaned_data['name']
                if Recipe.objects.filter(name=name).exists():
                    messages.error(request, f"A recipe with the name '{name}' already exists!")
                    return redirect('add_recipe')  # Redirect to the add recipe page again
                else:
                    form.save()  # Save the new recipe
                    messages.success(request, "Recipe added successfully!")
                    return redirect('list_recipes')  # Redirect to the recipe list page
            except IntegrityError:
                # In case there are other database integrity issues
                messages.error(request, "An error occurred while adding the recipe. Please try again.")
                return redirect('add_recipe')  # Redirect to the add recipe page again
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


# This function retrieves a specific recipe from the database using the `recipe_id` parameter.
# It then deletes the recipe using the `delete()` method and adds a success message to notify the user.
# After the recipe is deleted, the user is redirected to the recipe list page ('list_recipes').
def delete_recipe(request, recipe_id):
    try:
        # Try to get the recipe by its ID
        recipe = Recipe.objects.get(pk=recipe_id)
        # If found, delete the recipe
        recipe.delete()
        messages.success(request, 'Recipe deleted successfully.')
    except ObjectDoesNotExist:
        # If the recipe does not exist, show an error message
        messages.error(request, 'Recipe not found.')
    
    # Redirect back to the recipe list page
    return redirect('list_recipes')


# This function handles the search for recipes.
# It retrieves the search query from the GET request parameters using 'q'.
# The recipes are filtered using the 'name' field with a case-insensitive match (`icontains`).
# It then renders the 'recipe/search_recipes.html' template, 
# passing the filtered recipes and the search query to the template for display.
def search_recipes(request):
    query = request.GET.get('q')
    recipes = Recipe.objects.filter(name__icontains=query)
    return render(request, 'recipe/search_recipes.html', {'recipes': recipes, 'query': query})
