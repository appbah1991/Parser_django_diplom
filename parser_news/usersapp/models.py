from django.contrib.auth.models import AbstractUser

from django.db import models


class Parser_User(AbstractUser):
        email = models.EmailField(unique='True')

