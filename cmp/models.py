from collections.abc import Iterable
from django.db import models

# Create your models here.
class Address(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    description = models.TextField(max_length=200)
    street = models.CharField(max_length=100)
    outdoor_number = models.IntegerField()
    indoor_number = models.IntegerField(null=True, blank=True)
    street2 = models.CharField(max_length=100)
    street3 = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.IntegerField()
    city = models.CharField(max_length=50,default='Veracruz')
    def __str__(self):
        return '{}'.format(self.name)
    def save(self):
        return super(Address, self).save()
    class Meta:
        verbose_name_plural = 'Direcciones'