from fnmatch import fnmatchcase
from django.db import models

class Member(models.Model):
    usrname = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    apples = models.FloatField()
    bananas = models.FloatField()

    def __str__(self):
        return self.usrname