from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True)
    profile_photo = models.ImageField(upload_to="users/profile_photo/", blank=True)

    def __str__(self) -> str:
        return self.get_full_name() or self.username
