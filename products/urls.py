from django.conf.urls.defaults import *

urlpatterns = patterns(
    'products.views',
    (r'^$', 'index'),
    (r'^(?P<category_string>[A-Za-z_,]+)/$', 'product_list')
)
