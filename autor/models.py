from django.db import models

# Create your models here.

class Autor(models.Model):
    id_autor = models.AutoField(primary_key=True)
    naran_autor = models.CharField(max_length=60)
    def __str__(self):
        return self.naran_autor