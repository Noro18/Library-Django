from django.db import models

# Create your models here.

class Membru(models.Model):

    KATEGORIA_SEXU = [
        ('M', 'Mane'),
        ('F', 'Feto'),
    ]

    id_membru = models.AutoField(primary_key=True)
    naran_membru = models.CharField(max_length=100)
    hela_fatin = models.CharField(max_length=50)
    sexu = models.CharField(max_length=5, choices=KATEGORIA_SEXU, default='M')
    data_moris = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return {self.naran_membru}
