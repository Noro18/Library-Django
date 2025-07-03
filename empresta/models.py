from django.db import models
from membru.models import Membru
from livru.models import LivruKopia
from django.utils import timezone

class Empresta(models.Model):
    id_empresta = models.AutoField(primary_key=True)
    id_membru = models.ForeignKey("membru.Membru", on_delete=models.CASCADE)
    data_empresta = models.DateField(default=timezone.now)
    data_hatama = models.DateField(default=timezone.now)

    STATUS_CHOICES = [
        ('borrowing', 'Borrowing'),
        ('returned', 'Returned'),
        ('late', 'Late'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='borrowing')
    @property
    def is_overdue(self):
        return self.status == 'borrowing' and self.data_hatama < timezone.now().date()

    @property
    def display_status(self):
        if self.is_overdue:
            return 'late'
        return self.status
    def __str__(self):
        return f"Empresta {self.id_empresta} - {self.id_membru} - {self.status}"

class Empresta_Detail(models.Model):
    id_detail = models.AutoField(primary_key=True)
    id_empresta = models.ForeignKey('empresta.Empresta', on_delete=models.CASCADE)
    id_kopia = models.ForeignKey('livru.LivruKopia', on_delete=models.CASCADE)
    data_hatama_actual = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Detail {self.id_detail} - Empresta {self.id_empresta_id} - Kopia {self.id_kopia_id}"