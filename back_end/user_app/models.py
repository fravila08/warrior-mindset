from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import AppUserManager


# Create your models here.
class AppUser(AbstractUser):
    first_name: str = models.CharField(max_length=50)
    last_name: str = models.CharField(max_length=50)
    email: str = models.EmailField(unique=True, null=False, blank=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: list = []

    objects = AppUserManager()

    def __str__(self) -> str:
        return f"{self.first_name + ' ' + self.last_name if self.last_name and self.first_name else self.email}"
