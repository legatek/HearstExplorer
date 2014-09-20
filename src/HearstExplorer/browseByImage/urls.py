from django.conf.urls import patterns, url

from browseByImage import views

urlpatterns = patterns('',
    url(r'^$', views.browse, name='browse'),
    url(r'?P<artifact_id>\w+', views.detail, name='detail'),
)