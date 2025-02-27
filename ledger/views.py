from django.shortcuts import render
from .models import Recipe


def show_recipes(request):
    recipes = Recipe.objects.all()
    context = {
        "recipes": recipes
    }
    return render(request, "recipes/recipe-list.html", context)


def show_ingredients(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    context = {
        "recipes": recipe,
    }
    return render(request, "recipes/recipe-detail.html", context)