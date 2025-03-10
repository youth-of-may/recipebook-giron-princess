from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100, default="user")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("recipe-detail", args=[str(self.pk)])


class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("recipe-detail", args=[str(self.pk)])


class RecipeIngredient(models.Model):
    recipe_quantity = models.CharField(max_length=50)
    ingredients = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, related_name="recipe"
    )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="ingredients"
    )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.TextField(
        blank=True,
        validators=[MinLengthValidator(255, "the field must contain at least 255 characters.")],
    )
