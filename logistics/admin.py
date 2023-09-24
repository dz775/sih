from django.contrib import admin
from . import models

class Railway(admin.ModelAdmin):
	list_display = [field.name for field in models.Railway._meta.get_fields()]

admin.site.register(models.Railway, Railway)

# class Siding(admin.ModelAdmin):
#     list_display = ('name', 'location', 'capacity',)

# admin.site.register(models.Siding, Siding)

class CoalStock(admin.ModelAdmin):
	list_display = [field.name for field in models.CoalStock._meta.get_fields()]

admin.site.register(models.CoalStock, CoalStock)
