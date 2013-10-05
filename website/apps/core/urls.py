from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from website.apps.core.forms import ContactForm

from contact_form.views import ContactFormView


urlpatterns = patterns(
    'website.apps.core.views',
    url(
        r'^$',
        'home',
        name='home'
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
)
