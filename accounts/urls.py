from django.urls import path, include
from django.contrib.auth.views import LogoutView, PasswordResetCompleteView

from accounts.views import (
    CustomView,
    CustomPasswordReset,
    CustomPasswordResetDone,
    CustomPasswordResetConfirm,
)

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/login", CustomView.as_view(), name="login"),
    path("accounts/logout", LogoutView.as_view(next_page="login"), name="logout"),
    path("accounts/password_reset", CustomPasswordReset.as_view(), name="password_reset"),
    path(
        "accounts/reset/<uidb64>/<token>/",
        CustomPasswordResetConfirm.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "accounts/password_reset/done",
        CustomPasswordResetDone.as_view(),
        name="password_reset_done",
    ),
    path(
        "accounts/reset/complete",
        PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"),
        name="password_reset_complete",
    ),
]