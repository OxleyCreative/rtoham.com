from django.db import models

class PictureValidators:
    @staticmethod
    def validate_aspect_ratio(image_value):
        """
        Validates that the aspect ratio of the image is 4:3.
        """
        from django.core.exceptions import ValidationError
        if image_value.width / 4 != image_value.height / 3:
            raise ValidationError("The image must have a 4:3 aspect ratio.")

class Picture(models.Model):
    created_at = models.DateTimeField("created at", auto_now_add=True)
    modified_at = models.DateTimeField("modified at", auto_now=True)
    original_image = models.ImageField(upload_to="images/originals",
                                       height_field="original_height",
                                       width_field="original_width",
                                       validators=
                                       [PictureValidators.validate_aspect_ratio])
    image = models.ImageField(upload_to="images",
                              height_field="height",
                              width_field="width",
                              validators=
                              [PictureValidators.validate_aspect_ratio])
    thumbnail = models.ImageField(upload_to="images/thumbnails",
                                  height_field="thumbnail_height",
                                  width_field="thumbnail_width",
                                  validators=
                                  [PictureValidators.validate_aspect_ratio])
    alt_text = models.TextField()
    original_width = models.IntegerField()
    original_height = models.IntegerField()
    width = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    thumbnail_width = models.IntegerField(null=True)
    thumbnail_height = models.IntegerField(null=True)

    def __unicode__(self):
        return self.alt_text

    class Meta:
      app_label = 'products'
    

