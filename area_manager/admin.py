from django.contrib import admin

from .models import Country, Region, NaturalReserve


# Register your models here.
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name', 'country')


class NaturalReserveAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# Enregistrement des modèles avec leurs configurations d'administration personnalisées
admin.site.register(Country, CountryAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(NaturalReserve, NaturalReserveAdmin)
