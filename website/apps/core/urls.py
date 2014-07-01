from django.conf.urls import patterns, url, include
from django.utils.translation import ugettext
from django.views.generic import TemplateView

from contact_form.views import ContactFormView
from preferences import preferences

from website.apps.core.forms import ContactForm
from website.apps.core.views import GenericContentView


urlpatterns = patterns(
    'website.apps.core.views',
    url(
        r'^$',
        'home',
        name='home'
    ),
    url(
        r'^about/$',
        GenericContentView.as_view(
            title=ugettext('About Us'),
            content=lambda: preferences.GeneralPreferences.about_us
        ),
        name='about-us'
    ),
    # contact form urls
    url(
        r'^contact/$',
        ContactFormView.as_view(form_class=ContactForm),
        name='contact_form'
    ),
    url(
        r'^sent/$',
        TemplateView.as_view(
           template_name='contact_form/contact_form_sent.html'
        ),
        name='contact_form_sent'
    ),
    # form builder urls
    url(r'^forms/', include('forms_builder.forms.urls')),
)
