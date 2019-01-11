from django.db import models
from django.urls import reverse
# Create your models here.

class Hospital(models.Model):
    name = models.CharField(max_length=50, db_index = True)
    slug = models.SlugField(max_length=150, db_index = True)
    long = models.DecimalField(max_digits=50, decimal_places=20)
    lat = models.DecimalField(max_digits=50, decimal_places=20)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'hospital'
        verbose_name_plural = 'hospitals'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('hospital:doctor_list_by_category',args = [self.slug])


class Doctor(models.Model):
    hospital = models.ForeignKey(Hospital, related_name = 'doctors', on_delete = models.CASCADE)
    name = models.CharField(max_length = 100, db_index = True)
    slug = models.SlugField(max_length = 150, db_index = True)
    address = models.TextField(blank = True)
    description = models.TextField(blank = True)
    available = models.BooleanField(blank = True)
    phoneno = models.DecimalField(max_digits= 10, decimal_places=2)
    dob = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to = 'doctors/', blank = True)

    class Meta:
        ordering = ('name',)
        index_together = (('id','slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('hospital:doctor_detail', args=[self.id,self.slug])



class Ambulance(models.Model):
    hospital = models.ForeignKey(Hospital,  on_delete = models.CASCADE)
    driver_name = models.CharField(max_length = 100, db_index = True)
    ambulance_no = models.CharField(max_length = 100, db_index = True)
    slug = models.SlugField(max_length = 150, db_index = True)
    available = models.BooleanField(blank = True)
    phoneno = models.DecimalField(max_digits= 10, decimal_places=2)

    class Meta:
        ordering = ('driver_name',)
        index_together = (('slug'),)

    def __str__(self):
        return self.driver_name

    def get_absolute_url(self):
        return reverse('hospital:ambulance_detail', args=[self.id,self.slug])
