from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    user_id = models.UUIDField(primary_key=True, editable=False)
    

