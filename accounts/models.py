from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.TextField(
        blank=True,
        validators=[MinLengthValidator(255, "The field must contain at least 250 characters.")],
    )
