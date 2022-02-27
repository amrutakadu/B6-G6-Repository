from django.db import models

# Create your models here.

class Credentials(models.Model):
    uname = models.CharField(max_length = 100, null = True)
    pswd = models.CharField(max_length = 100, null = True)
    email = models.CharField(max_length = 20, null = True)

class gitModel(models.Model):
    gitcmd = models.CharField(max_length = 50, null = True)