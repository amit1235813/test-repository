from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'eduapp.views.home', name='home'),
    url(r'^page2_1/$', 'eduapp.views.page2_1', name='page2_1'),
    url(r'^about-us/$', 'eduapp.views.aboutus', name='aboutus'),
    url(r'^questionlook/$', 'eduapp.views.questionlook', name='questionlook'),
    url(r'^a05_02/$', 'eduapp.views.a05_02', name='a05_02'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^magicplace/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root = settings.MEDIA_ROOT)
