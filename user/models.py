from django.db import models
from rol.models import Rol
from country.models import Country
from idiom.models import Idiom
from theme.models import Theme

# Create your models here.


class User(models.Model):
    login = models.CharField(unique=True, max_length=45)
    first_name = models.CharField(db_column='firstName', max_length=45)  # Field name made lowercase.
    middle_name = models.CharField(db_column='middleName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='lastName', max_length=45)  # Field name made lowercase.
    mothers_name = models.CharField(db_column='mothersName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(max_length=45)
    gender = models.CharField(max_length=1, blank=True, null=True)
    mail = models.CharField(max_length=45, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    fk_rol = models.ForeignKey(Rol, models.CASCADE, db_column='fk_rol')
    fk_country = models.ForeignKey(Country, models.DO_NOTHING, db_column='fk_country')
    fk_idiom = models.ForeignKey(Idiom, models.DO_NOTHING, db_column='fk_idiom')
    fk_theme = models.ForeignKey(Theme, models.DO_NOTHING, db_column='fk_theme')

    def __str__(self):
        return self.login

        class Meta:
            managed = False
            db_table = 'user'


