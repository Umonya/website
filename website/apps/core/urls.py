from django.conf.urls import patterns, url


urlpatterns = patterns(
    'website.apps.core.views',
    url(r'^$', 'home', name='home')
)
