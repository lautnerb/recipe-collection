from django.contrib import admin
from recipe_collection.models import Category, DietLabel, Reference, Ingredient, \
    Spice, TriedCategory, Recipe

admin.site.register(Category)
admin.site.register(DietLabel)
admin.site.register(Reference)
admin.site.register(Ingredient)
admin.site.register(Spice)
admin.site.register(TriedCategory)
admin.site.register(Recipe)
