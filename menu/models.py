from django.db import models
from rol.models import Rol
# Create your models here.


class Menu(models.Model):
    code_menu = models.CharField(max_length=3)
    name_menu = models.CharField(max_length=45)
    des_menu = models.TextField(blank=True, null=True)
    url_menu = models.CharField(max_length=45)
    fk_menu = models.ForeignKey('self', models.DO_NOTHING, db_column='fk_menu', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu'


class Permission(models.Model):
    active = models.IntegerField(blank=True, null=True)
    fk_rol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='fk_rol')
    fk_menu = models.ForeignKey(Menu, models.DO_NOTHING, db_column='fk_menu')

    def __str__(self):
        return '%s %s' %(self.rol.name_rol, self.menu.name_menu)

    class Meta:
        managed = False
        db_table = 'permission'