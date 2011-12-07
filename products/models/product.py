from django.db import models
from picture import Picture

class Product(models.Model):
    CATEGORY_CHOICES = [
        (u"USED_EQUIPMENT", u"Used Equipment"),
        (u"MANUALS", u"Manuals"),
        (u"PARTS", u"Parts"),
        (u"ACCESSORIES", u"Accessories"),
        (u"REPAIRS", u"Repairs"),
    ]
    created_at = models.DateTimeField("created at", auto_now_add=True)
    modified_at = models.DateTimeField("modified at", auto_now=True)
    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES)
    # Use a related_name to distinguish between the reverse accessor for
    # image and images.
    image = models.ForeignKey(
        Picture, related_name="main_product_set", null=True, blank=True)
    images = models.ManyToManyField(Picture, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        null=True,
        blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(unique=True, db_index=True)

    def url(self):
        return '/product/' + self.slug + '/'

    placeholder_images = {
        'USED_EQUIPMENT': 'usedplace',
        'MANUALS': 'manualplace',
        'PARTS': 'partplace',
        'REPAIRS': 'repairplace',
        'ACCESSORIES': 'accessoryplace'
        }
    
    def placeholder_image(self):
        return '/static/images/' + self.placeholder_images[self.category] + 'l.png'

    def placeholder_thumbnail(self):
        return '/static/images/' + self.placeholder_images[self.category] + '.png'

    def __unicode__(self):
        return self.title

    class Meta:
        app_label = 'products'
