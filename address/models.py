from django.db import models
from user.models import User
from city.models import City
# Create your models here.


class Address(models.Model):
    address = models.TextField()
    race = models.CharField(max_length=45, blank=True, null=True)
    street = models.CharField(max_length=45, blank=True, null=True)
    avenue = models.CharField(max_length=45, blank=True, null=True)
    sidewalk = models.CharField(max_length=45, blank=True, null=True)
    building = models.CharField(max_length=45, blank=True, null=True)
    floor = models.CharField(max_length=45, blank=True, null=True)
    name_residence = models.CharField(max_length=45, blank=True, null=True)
    number_residence = models.CharField(max_length=45, blank=True, null=True)
    suburb = models.CharField(max_length=45, blank=True, null=True)
    fk_user = models.ForeignKey(User, models.DO_NOTHING, db_column='fk_user')
    fk_city = models.ForeignKey(City, models.DO_NOTHING, db_column='fk_city')

    class Meta:
        managed = False
        db_table = 'address'