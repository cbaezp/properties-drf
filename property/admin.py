from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import (
    Category,
    Property,
    PropertyFeature,
    PropertyImage,
    PropertySpecification,
    PropertySpecificationValue,
)

admin.site.register(Category, MPTTModelAdmin)


class PropertySpecificationInline(admin.TabularInline):
    model = PropertySpecification


@admin.register(PropertyFeature)
class PropertyFeatureAdmin(admin.ModelAdmin):
    inlines = [
        PropertySpecificationInline,
    ]


class PorductImageInline(admin.TabularInline):
    model = PropertyImage


class PropertySpecificationValueInline(admin.TabularInline):
    model = PropertySpecificationValue


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertySpecificationValueInline, PorductImageInline]
