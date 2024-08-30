from django.contrib import admin
from . models import City, CityDescription
# Register your models here.
class CityDescriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'city_description', 'best_food', 'best_place_to_visit', 'rating')
    search_fields = ('name__city_name', 'city_description', 'best_food', 'best_place_to_visit')

admin.site.register(City)
admin.site.register(CityDescription, CityDescriptionAdmin)