from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
    def login(self, postData):
        pass
    def register(self, postData):
        pass
class User(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()
