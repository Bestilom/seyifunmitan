    from django.db import models

# Create your models here.                
class MenuItem(models.model):
     name = models.CharField(max_length=255)
     price = models.IntegerField( )
