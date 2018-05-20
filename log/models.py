from django.db import models
from user.models import User
# Create your models here.


class Log(models.Model):
    des_log = models.TextField()
    fecha = models.DateTimeField(blank=True, null=True)
    fk_user = models.ForeignKey(User, models.DO_NOTHING, db_column='fk_usuario')
    cod_menu = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log'
