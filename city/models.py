from django.db import models
from province.models import Province
# Create your models here.


class City(models.Model):
    name_city = models.CharField(max_length=45)
    code_area = models.CharField(max_length=45, blank=True, null=True)
    code_postal = models.CharField(max_length=45, blank=True, null=True)
    fk_province = models.ForeignKey(Province, models.DO_NOTHING, db_column='fk_provincia')

    class Meta:
        managed = False
        db_table = 'city'

