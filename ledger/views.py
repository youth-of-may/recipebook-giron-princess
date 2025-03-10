from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
)
from django.contrib.auth.decorators import login_required

from .models import Recipe


def show_recipes(request):
    recipes = Recipe.objects.all()
    context = {"recipes": recipes}
    return render(request, "recipes/recipe-list.html", context)


@login_required
def show_ingredients(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    context = {"recipes": recipe}
    return render(request, "recipes/recipe-detail.html", context)


class CustomView(LoginRequiredMixin, TemplateView):
    template_name = "registration/login.html"
    redirect_field_name = "accounts/login"


class CustomPasswordReset(PasswordResetView):
    template_name = "registration/password_reset_form.html"
    email_template_name = "registration/password_reset_email.html"
    success_url = "password_reset/done"


class CustomPasswordResetDone(PasswordResetDoneView):
    template_name = "registration/password_reset_done.html"


class CustomPasswordResetConfirm(PasswordResetConfirmView):
    template_name = "registration/password_reset_confirm.html"
    success_url = "password_reset/complete"