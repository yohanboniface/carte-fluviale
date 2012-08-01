from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.decorators import permission_required

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from chickpea.urls import urlpatterns

urls_to_decorate = {
    "marker_update": permission_required('marker.can_change'),
    "marker_add": permission_required('marker.can_add')
}

for urlpattern in urlpatterns:
    if urlpattern.name in urls_to_decorate:
        urlpattern._callback = urls_to_decorate[urlpattern.name](urlpattern.callback)

urlpatterns += patterns('',
    # Examples:
    # url(r'^$', 'heron.views.home', name='home'),
    # url(r'^/', include('chickpea.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()
