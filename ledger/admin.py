from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient


class IngredientInline(admin.StackedInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    search_fields = ('name',)
    list_display = ('name',)
    fieldsets = [
        ('Task Information', {
            'fields': ['name'],
        }),
    ]
    inlines = [IngredientInline]


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    search_fields = ('name',)
    list_display = ('name',)
    fieldsets = [
        ('Task Information', {
            'fields': ['name'],
        }),
    ]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
