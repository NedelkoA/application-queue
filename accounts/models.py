from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class Person(AbstractBaseUser, PermissionsMixin):
    pass
