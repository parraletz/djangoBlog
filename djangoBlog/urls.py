from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoBlog.views.home', name='home'),
    # url(r'^djangoBlog/', include('djangoBlog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^alumnos/', 'djangoBlog.principal.views.alumnos'),
    url(r'^addAlumnos/', 'djangoBlog.principal.views.addAlumnos'),
    url(r'^admin/', include(admin.site.urls)),
)
