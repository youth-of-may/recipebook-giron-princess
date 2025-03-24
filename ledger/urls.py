from django.urls import path
from . import views

urlpatterns = [
    path("recipes/list", views.show_recipes, name="recipes"),
    path("recipe/<int:pk>/", views.show_ingredients, name="recipe-detail"),
    path("recipe/<int:pk>/add_image", views.add_recipe_image, name="recipe-add-image"),
    path("recipe/add/", views.add_recipes, name="recipe-add"),
]