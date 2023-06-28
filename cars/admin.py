from django.contrib import admin
from .models import Car


class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'year', 'model_year', 'value')
    search_fields = ('model',)

admin.site.register(Car, CarAdmin)
