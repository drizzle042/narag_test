from django.db import models
from django.contrib.auth.hashers import make_password


class Code(models.Model):
    code = models.CharField(max_length=20, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


class Files(models.Model):
    name = models.CharField(max_length=50, unique=True)
    file = models.FileField(upload_to='files/% Y/', unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
