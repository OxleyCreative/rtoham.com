from django.db import models

class Article(models.Model):
    created_at = models.DateTimeField("created at", auto_now_add=True)
    modified_at = models.DateTimeField("modified at", auto_now=True) 
    text = models.TextField()
    show_on_homepage = models.BooleanField(
        "show on homepage", default=False)
    order = models.IntegerField(default=0)
    title = models.CharField(max_length=128)
    link = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(unique=True, db_index=True)
    
    def __unicode__(self):
        return self.title

    def article_link(self):
        """
        Returns the correct link for an article, which will be the
        link field if it is populated - otherwise routed slug field.
        """
        return self.link if self.link != "" else "/articles/" + self.slug

    class Meta:
        ordering = ["order", "-created_at"]
        app_label = 'home'
