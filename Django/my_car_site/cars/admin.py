from django.contrib import admin

from .models import Car

class CarAdmin(admin.ModelAdmin):
    fields = ["year","brand"]
admin.site.register(Car,CarAdmin)
