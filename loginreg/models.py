from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

# Create your models here.

class UserProfile(models.Model):
    user= models.OneToOneField(User)

    def __str__(self):
        return '%s' % (self.user)