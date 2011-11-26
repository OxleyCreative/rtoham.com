from django.db import models

class Picture(models.Model):
    created_at = models.DateTimeField("created at", auto_now_add=True)
    modified_at = models.DateTimeField("modified at", auto_now=True)
    image = models.ImageField(upload_to="images",
                              height_field="height",
                              width_field="width")
    alt_text = models.TextField()
    width = models.IntegerField()
    height = models.IntegerField()

    def __unicode__(self):
        return self.alt_text

    class Meta:
      app_label = 'products'
    

