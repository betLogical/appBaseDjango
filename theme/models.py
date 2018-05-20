from django.db import models

# Create your models here.


class Theme(models.Model):
    code_theme = models.CharField(max_length=3)
    name_theme = models.CharField(max_length=45)
    url_css = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'theme'

