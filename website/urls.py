from django.conf.urls import patterns, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin


admin.autodiscover()


urlpatterns = i18n_patterns(
    '',
    (r'^', include('website.apps.core.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^ckeditor/', include('ckeditor.urls')),
)

# urls exempt from language prefix
urlpatterns += patterns(
    '',
   (r'^i18n/', include('django.conf.urls.i18n')),
)
