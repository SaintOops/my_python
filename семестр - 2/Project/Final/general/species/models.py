from django.db import models

# Create your models here.

class Animal (models.Model):
    title= models.CharField(max_length=100)
    image= models.ImageField(upload_to='')
    describ= models.CharField(max_length=1000)
    date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title