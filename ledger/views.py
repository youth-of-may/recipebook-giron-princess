from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Recipe
from .forms import RecipeForm, RecipeImageForm

@login_required
def show_recipes(request):
    recipes = Recipe.objects.all()
    context = {"recipes": recipes}
    return render(request, "recipes/recipe-list.html", context)


@login_required
def show_ingredients(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    context = {"recipes": recipe}
    return render(request, "recipes/recipe-detail.html", context)


@login_required
def add_recipes(request):
    form = RecipeForm()

    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            return redirect("recipe-detail", pk=recipe.pk)

    context = {"form": form}
    return render(request, "recipes/recipe-add.html", context)


@login_required
def add_recipe_image(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    if request.method == "POST":
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.recipe = recipe
            image.save()
            return redirect("recipe-detail", pk=recipe.pk)
    else:
        form = RecipeImageForm()

    context = {"form": form, "recipe": recipe}
    return render(request, "recipes/recipe-add-image.html", context)