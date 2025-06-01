from django.db import models

# Create your models here.

class Kategoria(models.Model):
    id_kategoria = models.AutoField(primary_key=True)
    naran_kategoria = models.CharField(max_length=60)
    def __str__(self):
        return self.naran_kategoria
    

class Livru(models.Model):
    id_livru = models.AutoField(primary_key=True)
    titulu_livru = models.CharField(max_length=60)
    isbn = models.CharField(max_length=20)
    id_kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE, null=True, blank=True)
    id_autor = models.ForeignKey("autor.Autor", on_delete=models.CASCADE, null=True, blank=True)
    id_publisher = models.ForeignKey("publisher.Publisher", on_delete=models.CASCADE, null=True, blank=True)
    data_publica = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    
    @property
    def total_copia(self):
        return self.kopia.count()

    def __str__(self):
        return (f"{self.titulu_livru} husi author {self.id_autor}")

    
class LivruKopia(models.Model):
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
        
    )

    id_kopia = models.AutoField(primary_key=True)
    id_livru = models.ForeignKey(Livru, on_delete=models.CASCADE, related_name='kopia')
    barcode = models.CharField(max_length=20)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return f"{self.id_kopia} {self.barcode}"
    