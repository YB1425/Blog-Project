from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.hashers import make_password

class UserTable (models.Model):
    username = models.CharField(max_length=255, unique=True)
    email_address = models.EmailField(unique=True)
    password = models.CharField(max_length=150)

    def save(self, *args, **kwargs):
        if not self.pk or 'password' in self.__dict__:
            self.password = make_password(self.password)
        super(UserTable, self).save(*args, **kwargs)

    def __str__(self):
        return self.username