from django.conf.urls.defaults import *

urlpatterns = patterns('home.views',
    (r'(?P<article_id>\d+)/$', 'detail')
)
