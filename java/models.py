from django.db import models

# Create your models here.
class Kik(models.Model):

    liga = models.ImageField(upload_to='media')
    lige = models.ImageField(upload_to='media')
    
    narxi = models.IntegerField( null=True)
    narxi1 = models.IntegerField( null=True)    
    namc = models.CharField(max_length=200 , null=True)
    tavk = models.CharField(max_length=200 , null=True)
    namr = models.CharField(max_length=200 , null=True)
    tavt = models.CharField(max_length=200 , null=True)
    aktiv = models.BooleanField(default=True)


    def __str__(self):
        return self.namc