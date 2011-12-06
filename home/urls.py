from django.conf.urls.defaults import *

urlpatterns = patterns('home.views',
    (r'^(?P<article_id>\d+)/$', 'detail'),
    (r'^(?P<article_slug>[A-Za-z0-9-]+)/$', 'detail_with_slug'),
)
