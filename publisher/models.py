from django.db import models

# Create your models here.

class Publisher(models.Model):
    id_publisher = models.AutoField(primary_key=True)
    naran_publisher = models.CharField(max_length=60)
    enderesu = models.CharField(max_length=50, null=True, blank=True, default="")
    email = models.EmailField(max_length=254, null=True, blank=True, default="")
    nu_telf = models.CharField(max_length=50, null=True, blank=True, default="")
    def __str__(self):
        return self.naran_publisher