from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Foydalanuvchi(AbstractUser):
    ism=models.CharField(max_length=25)
    yosh=models.PositiveSmallIntegerField()
    first_name = None
    last_name = None
    last_login = None