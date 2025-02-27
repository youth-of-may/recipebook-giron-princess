from django.db import models
from django.urls import reverse


class Recipe(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipe-detail', args=[str(self.pk)])


class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipe-detail', args=[str(self.pk)])


class RecipeIngredient(models.Model):
    recipe_quantity = models.IntegerField()
    ingredients = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='recipe')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
