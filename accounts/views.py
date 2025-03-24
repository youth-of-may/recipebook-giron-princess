from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
)
from django.views.generic import TemplateView

# Custom authentication views
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