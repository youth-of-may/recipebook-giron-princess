from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient, RecipeImage


class IngredientInline(admin.StackedInline):
    model = RecipeIngredient


class RecipeImageInline(admin.StackedInline):
    model = RecipeImage
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    search_fields = ("name",)
    list_display = ("name", "author", "created_on")
    fieldsets = [
        ("Recipe Information", {"fields": ["name"]}),
    ]
    inlines = [IngredientInline, RecipeImageInline]


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    search_fields = ("name",)
    list_display = ("name",)
    fieldsets = [
        ("Ingredient Information", {"fields": ["name"]}),
    ]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)