from django.db import models
from hospital.models import Hospital
from django.urls import reverse
# Create your models here.

class Ambulance(models.Model):
    hospital = models.ForeignKey(Hospital, related_name = 'hospitals', on_delete = models.CASCADE)
    driver_name = models.CharField(max_length = 100, db_index = True)
    ambulance_no = models.CharField(max_length = 100, db_index = True)
    slug = models.SlugField(max_length = 150, db_index = True)
    available = models.BooleanField(blank = True)
    phoneno = models.DecimalField(max_digits= 10, decimal_places=2)

    class Meta:
        ordering = ('driver_name',)
        index_together = (('slug'),)

    def __str__(self):
        return self.name
