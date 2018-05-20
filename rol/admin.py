from django.contrib import admin
from .models import Rol
# Register your models here.


@admin.register(Rol)
class AdminUser(admin.ModelAdmin):
    list_display = ('code_rol', 'name_rol', 'des_rol')
    list_filter = ('code_rol',)

