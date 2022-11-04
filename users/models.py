from django.db import models
from django.contrib.auth import get_user_model, models

class User(models.AbstractUser):
    pass

    def __str__(self):
        return self.email
