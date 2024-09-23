# gestion_utilisateurs/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Ajoutez des champs supplémentaires si nécessaire

    def __str__(self):
        return self.username
