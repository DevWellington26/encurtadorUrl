from django.db import models

# Create your models here.
class Link(models.Model):
    nome = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
