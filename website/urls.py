from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin


admin.autodiscover()


urlpatterns = i18n_patterns(
    '',
    url(r'^$', include('website.apps.core.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
)

# urls exempt from language prefix
urlpatterns += patterns(
    '',
   url(r'^i18n/', include('django.conf.urls.i18n')),
)
