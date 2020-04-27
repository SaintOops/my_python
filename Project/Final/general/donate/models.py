from django.db import models

# Create your models here.

class Paydata (models.Model):
    name= models.CharField(max_length=30)
    surname= models.CharField(max_length=30)
    cardnum= models.CharField(max_length=16)
    cvc= models.CharField(max_length=3)
    cardvalid= models.CharField(max_length=6)
    money=models.CharField(max_length=100)

    def __str__(self):
        return self.money
