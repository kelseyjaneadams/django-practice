# Generated by Django 5.1.3 on 2024-12-06 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_alter_recipe_name'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='recipe',
            index=models.Index(fields=['name', 'ingredients', 'instructions'], name='recipe_reci_name_4add7a_idx'),
        ),
    ]