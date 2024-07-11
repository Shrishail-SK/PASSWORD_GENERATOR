

from django.db import models

class AmazonPassword(models.Model):
    password = models.CharField(max_length=100)

class FlipkartPassword(models.Model):
    password = models.CharField(max_length=100)

class AWSPassword(models.Model):
    password = models.CharField(max_length=100)
