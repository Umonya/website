from django.utils import timezone

from preferences import preferences
from forms_builder.forms.models import STATUS_PUBLISHED

from website.apps.core.models import StudentRegistrationPreferences


def form_is_published(form):
    now = timezone.now()
    if form.status != STATUS_PUBLISHED:
        return False
    elif form.publish_date and now < form.publish_date:
        return False
    elif form.expiry_date and now > form.expiry_date:
        return False
    return True


def registration(request):
    try:
        reg_prefs = preferences.StudentRegistrationPreferences
        return {
            'REGISTRATION_OPEN': (reg_prefs.registration_status == 'open'
                                  and reg_prefs.registration_form
                                  and form_is_published(reg_prefs.registration_form)),
            'REGISTRATION_FORM': reg_prefs.registration_form
        }
    except StudentRegistrationPreferences.DoesNotExist:
        return {'REGISTRATION_OPEN': False}
