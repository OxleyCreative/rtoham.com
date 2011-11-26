from products.models import Picture
from django.contrib import admin

class PictureAdmin(admin.ModelAdmin):
    fields = ['alt_text', 'original_image']

admin.site.register(Picture, PictureAdmin)
