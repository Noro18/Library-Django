from django.db import models

# Create your models here.

class Autor(models.Model):
    id_autor = models.AutoField(primary_key=True)
    naran_autor = models.CharField(max_length=60)
    data_moris = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    nasionalidade =  models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.naran_autor