from django.contrib import admin
from webapp.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'description', 'category', 'balance', 'cost']
    list_filter = ['name']
    list_display_links = ['pk', 'description']
    search_fields = ['name', 'description']
    fields = ['name', 'description', 'category', 'balance', 'cost']
    readonly_fields = ['balance', 'cost']



admin.site.register(Product, ProductAdmin)

