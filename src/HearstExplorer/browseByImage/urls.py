from django.conf.urls import patterns, url

from browseByImage import views

urlpatterns = patterns('',
    url(r'^$', views.browse, name='browse'),
    url(r'(?P<artifact_id>[a-zA-Z0-9\-\.,]+)', views.detail, name='detail'),
)