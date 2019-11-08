from django.contrib import admin
# the module name is app_name.models

# Register your models to admin site, then you can add, edit, delete and search your models in Django admin site.
from places.models import Place

class PlaceAdmin(admin.ModelAdmin):
    exclude = ('is_active', 'uuid')

admin.site.register(Place, PlaceAdmin)