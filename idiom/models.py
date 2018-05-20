from django.db import models

# Create your models here.


class Idiom(models.Model):
    iso = models.CharField(max_length=3)
    name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'idiom'
