from django.contrib import admin

from .models import Categories, Products
# Register your models here.


@admin.register(Categories)
class AdminCategories(admin.ModelAdmin):
    prepulated_fields = {'slug': ['name']}

@admin.register(Products)
class AdminProducts(admin.ModelAdmin):
    prepulated_fields = {'slug': ['name']}