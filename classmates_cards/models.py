from django.db import models


class CardModel(models.Model):
    number = models.IntegerField()
    email = models.EmailField(null=True)


class ClassmateData(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)