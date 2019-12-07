# Create your models here.
from django.db import models


# Create your models here.

class Product(models.Model):
    Code = models.CharField(max_length=50)
    Name = models.CharField(max_length=100)
    Price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return u'%s - %s' % (self.Code, self.Name)
