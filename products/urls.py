from django.conf.urls.defaults import *

urlpatterns = patterns(
    'products.views',
    (r'$', 'product_list'),
    (r'(?P<categories>[A-Za-z_,]+)', 'product_list')
)
