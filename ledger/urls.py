from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name= 'index'),
    path('recipes/list', views.showrecipes, name = 'recipes'),
    path('recipe/1', views.recipeone, name = "first_recipe"),
    path('recipe/2', views.recipetwo, name = "second_recipe")
]
