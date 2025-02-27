from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_recipes, name='recipes'),
    path('recipes/<int:pk>/', views.show_ingredients, name='recipe-detail'),
]
