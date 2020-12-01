from django.contrib import admin
from .models import ProductModel

@admin.register(ProductModel)
class ProAdmin(admin.ModelAdmin):
    list_display = ['no','name', 'price', 'quantity', 'photo', 'pdate']