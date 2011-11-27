from products.models import Picture
from products.models import Product
from django.contrib import admin

class PictureAdmin(admin.ModelAdmin):
    fields = ['alt_text', 'original_image']

class ProductAdmin(admin.ModelAdmin):
    fields = [
        'title', 'description', 'category',
        'image', 'images', 'price',
        'quantity', 'slug'
    ]
    prepopulated_fields = {'slug': ('category', 'title',)}

admin.site.register(Picture, PictureAdmin)
admin.site.register(Product, ProductAdmin)
