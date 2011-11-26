from products.models import Picture
from django.contrib import admin

class PictureAdmin(admin.ModelAdmin):
    fields = ['alt_text', 'image']

admin.site.register(Picture, PictureAdmin)
