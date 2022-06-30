from django.db import models

# Create your models here.
class myfriends(models.Model):
  name = models.CharField(max_length=100)
  sex = models.IntegerField(max_length=1)
  detail = models.TextField()