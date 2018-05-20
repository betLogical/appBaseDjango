from django.db import models

# Create your models here.


class Country(models.Model):
    code_country = models.CharField(max_length=3)
    name_country = models.CharField(max_length=45)
    code_phone = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.name_country

    class Meta:
        managed = False
        db_table = 'country'