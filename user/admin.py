from django.contrib import admin

from user.models import User

# Register your models here.
# admin.site.register(Product)


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ('login', 'first_name', 'mail')
    list_filter = ('fk_rol',)
