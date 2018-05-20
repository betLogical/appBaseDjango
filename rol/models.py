from django.db import models

# Create your models here.


class Rol(models.Model):
    code_rol = models.CharField(max_length=3)
    name_rol = models.CharField(max_length=45)
    des_rol = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name_rol

    class Meta:
        managed = False
        db_table = 'rol'
