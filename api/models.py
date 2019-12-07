from django.db import models


# Create your models here.

class Score(models.Model):
    usuario = models.CharField(max_length=100)
    score = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return u'%s' % self.usuario
