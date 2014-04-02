# coding: utf-8
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from lib_app.views import BookListView,BookDetailView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$',BookListView.as_view(), name='book_list'),
                       url(r'^book/(?P<pk>\d+)/$', BookDetailView.as_view(),name='book_detail'),
                       url(r'^book_edit/(?P<book_id>\d+)/$','lib_app.views.book_edit',name='book_edit'),
                       
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^admin/', include(admin.site.urls)),    
    
                       )
                                             
if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()


                       
