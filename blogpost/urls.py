from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^search/$', views.search, name='search'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.tags, name='tag'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^detail/(?P<id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^$', views.index, name='index'),
]