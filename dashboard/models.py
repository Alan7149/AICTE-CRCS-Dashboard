from django.db import models

# Create your models here.
SECTOR_TYPE = ((1, "Credit"), (2, "Agro"), (3, "Health/Hospital"), (4, 'Fisheries'), (5, "Cooperative Bank"), (6, "Industrial/Textile"), (7, "Marketing"), (8, "Housing"), (9, "Dairy"), (10, "Tourism"), (11, "Federation"), (12, "Construction"), (13, "Others"))

class SectorType(models.Model):
    sector_id = models.CharField(max_length=200, null=True, blank=True)
    sector_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.sector_name)

class Society(models.Model):
    sr_no = models.CharField(max_length=100, null=True, blank=True)
    society_name = models.CharField(max_length=200, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    district = models.CharField(max_length=100, null=True, blank=True)
    registration_date = models.DateField(null=True, blank=True)
    area_operation = models.CharField(max_length=100, null=True, blank=True)
    sector_type = models.ForeignKey(SectorType, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return str(self.society_name)