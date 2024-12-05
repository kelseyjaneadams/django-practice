from django.db import models

# Create your models here.

# name: A CharField for the recipe's name (max 200 characters).
# ingredients: A TextField for listing the ingredients.
# instructions: A TextField for the preparation instructions.
# __str__(self): A method that returns the recipe's name when the object is printed or displayed.
# The CharField type is used for shorter text fields with a maximum length, while TextField is suitable for longer text content without predefined limits.
class Recipe(models.Model):
    name = models.CharField(max_length=200, unique=True) # This ensures the name is unique
    ingredients = models.TextField()
    instructions = models.TextField()

    def __str__(self):
        return self.name