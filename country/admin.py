from django.contrib import admin
from .models import Country
# Register your models here.

@admin.register(Country)
class AdminCountry(admin.ModelAdmin):
    list_display = ('code_country', 'name_country', 'code_phone')
    list_filter = ('name_country',)
