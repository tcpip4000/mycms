from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^mycms/', include('mycms.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^search/$', 'search.views.search'),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
    (r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve',
                            { 'document_root': '/home/fulano/documents/workspace/mycms/media/js/tinymce/jscripts/tiny_mce' }),


    # flat pages urls
    (r'', include('django.contrib.flatpages.urls')),
)
