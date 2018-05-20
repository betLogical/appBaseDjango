from django.db import models
from country.models import Country
# Create your models here.


class Province(models.Model):
    code_province = models.CharField(max_length=3)
    name_province = models.CharField(max_length=45)
    fk_country = models.ForeignKey(Country, models.DO_NOTHING, db_column='fk_country')

    class Meta:
        managed = False
        db_table = 'province'
