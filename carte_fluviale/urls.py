from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.contrib.auth.decorators import permission_required

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from leaflet_storage.urls import urlpatterns
from leaflet_storage.views import MapView

# urls_to_decorate = {
#     "marker_update": permission_required('marker.can_change'),
#     "marker_add": permission_required('marker.can_add')
# }

# for urlpattern in urlpatterns:
#     if urlpattern.name in urls_to_decorate:
#         urlpattern._callback = urls_to_decorate[urlpattern.name](urlpattern.callback)

urlpatterns += patterns('',
    url(r'^$', MapView.as_view(), {"slug": "fluvial", "username": "ybon"}, name='fluvial_map'),
    url(r'^poupe/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()
