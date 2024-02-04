from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

from commons.base_model import BaseModel


class User(AbstractBaseUser, BaseModel):
    name = models.CharField()
    email = models.EmailField(unique=True, null=False, default=None)

    USERNAME_FIELD = "email"

    class Meta:
        db_table = "user"
        verbose_name = "User"
    
    def __str__(self):
        return self.email