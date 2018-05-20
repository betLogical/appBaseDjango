from django.db import models
from user.models import User

# Create your models here.


class Phone(models.Model):
    international_code = models.CharField(db_column='internationalCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    area_code = models.CharField(db_column='areaCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    number = models.CharField(max_length=10, blank=True, null=True)
    description = models.CharField(max_length=45, blank=True, null=True)
    fk_user = models.ForeignKey(User, models.DO_NOTHING, db_column='fk_user')

    class Meta:
        managed = False
        db_table = 'phone'
