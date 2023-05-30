from django.db import models

# Create your models here.

#Create model Image
class Image(models.Model):
    image = models.ImageField(upload_to='images/')

#class User(models.Model):





