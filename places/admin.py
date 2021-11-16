from django.contrib import admin
# the module name is app_name.models

# Register your models to admin site, then you can add, edit, delete and search your models in Django admin site.
from places.models import Image, Place

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

class PlaceAdmin(admin.ModelAdmin):
    exclude = ('is_active', 'uuid')
    inlines = [ImageInline, ]

admin.site.register(Place, PlaceAdmin)