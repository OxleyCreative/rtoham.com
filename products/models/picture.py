from django.db import models
import Image, os, tempfile
from django.core.files import File

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
    
    THUMBNAIL_SIZE = (120, 90)
    IMAGE_SIZE = (460, 345)

    def __unicode__(self):
        return self.alt_text

    def save(self, *args, **kwargs):
        if self.original_image != None:
            if not hasattr(self.thumbnail, "file"):
                self.populateResizedImage(self.THUMBNAIL_SIZE, self.thumbnail)
            if not hasattr(self.image, "file"):
                self.populateResizedImage(self.IMAGE_SIZE, self.image)
        super(Picture, self).save(*args, **kwargs)
        
    def populateResizedImage(self, size, attribute):
        self.original_image.open("rb")
        image = Image.open(self.original_image)
        name, ext = os.path.splitext(self.original_image.name)
        resized = image.resize(size, Image.ANTIALIAS)
        
        # Create a temporary file to save the resized image to.
        (temp_fd, temp_filepath) = tempfile.mkstemp(ext)
        # We'll have to close the file using the file descriptor and
        # re-open it using open, since file objects opened using
        # os.fdopen do not work with django File objects.
        os.close(temp_fd)
        temp_file = open(temp_filepath, "w+b")
        resized.save(temp_file)
        attribute.save(self.original_image.name,
                               File(temp_file),
                               save=False)
        temp_file.close()
        os.remove(temp_filepath)
        self.original_image.close()

    class Meta:
      app_label = 'products'
    

