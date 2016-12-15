from django.conf.urls import url
from blog.views import *
urlpatterns = [
        # Ex : /
        url(r"^$", PostLV.as_view(),name='index'),
        # ex : /post/ (same as /)
        url(r'^posts/$', PostLV.as_view(), name='post_list'),
        # ex post/django-example
        url(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'),

        # ex /archive/
        url(r'^archive/$', PostAV.as_view(), name='post_archive'),
        # ex /2012/
        url(r'^(?P<year>\d{4})/$', PostYAV.as_view(), name='post_year_archive'),
        # ex /2012/nov/
        url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', PostMAV.as_view(),
            name='post_month_archive'),
        # ex /2012/nov/10/
        url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', PostDAV.as_view(),
            name='post_day_archive'),

        # ex : /today/
        url(r'^today/$', PostTAV.as_view(), name='post_today_archive'),
        # ex: /tag/
        url(r'tag/$', TagTV.as_view(), name='tag_cloud'),
        # ex: /tag/tagname/
        url(r'tag/(?P<tag>[^/]+(?u))/$', PostTOL.as_view(), name='tagged_object_list'),
        # ex: /blog/search/
        url(r'^search/$',SearchFormView.as_view(),name='search'),
        ]
