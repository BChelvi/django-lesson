from django.contrib import admin
from .models import Animal, Species, Zone, Keeper


# Register your models here.
# Admin pour le modèle Animal avec des filtres avancés
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'species', 'diet', 'weight', 'zone')
    list_filter = ('species', 'diet', 'zone')
    search_fields = ('name', 'species__name')


# Admin pour le modèle Species
class SpeciesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'conservation_status')
    search_fields = ('name',)


# Admin pour le modèle Zone
class ZoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'climate', 'area')
    search_fields = ('name',)
    list_filter = ('climate',)

# Admin pour le modèle Keeper avec des filtres avancés
class KeeperAdmin(admin.ModelAdmin):
    list_display = ('name', 'hire_date')
    search_fields = ('name',)


# Enregistrement des modèles avec leurs configurations d'administration personnalisées
admin.site.register(Animal, AnimalAdmin)
admin.site.register(Species, SpeciesAdmin)
admin.site.register(Zone, ZoneAdmin)
admin.site.register(Keeper, KeeperAdmin)
