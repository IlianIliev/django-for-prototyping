from django.conf.urls import patterns, include, url


from {{ project_name }}.views import StaticPageView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$',
        StaticPageView.as_view(template_name='{{ project_name }}/home.html'),
        name='home'),
    url(r'^(?P<slug>[-\w]+)/$', StaticPageView.as_view(), name='page'),
)


from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = staticfiles_urlpatterns() + urlpatterns
