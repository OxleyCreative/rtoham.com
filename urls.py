from django.conf.urls import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'home.views.index'),
    (r'^articles/', include('home.urls')),
    (r'^products/', include('products.urls')),
    (r'^product/(?P<slug>[A-Za-z0-9_-]+)/', 'products.views.product'),
    (r'^about-us/', 'home.views.about_us'),

    # Uncomment the admin/doc line below to enable admin documentation:
    #(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
