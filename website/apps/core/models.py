from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

from preferences import preferences
from preferences.models import Preferences
from forms_builder.forms.models import Form, STATUS_PUBLISHED, STATUS_DRAFT


class ContactPreferences(Preferences):
    __module__ = 'preferences.models'
    raw_emails = models.TextField(
        default='',
        blank=True,
        verbose_name='email addresses',
        help_text='Contact form messages will be sent to these email addresses. Specify one per line.'
    )
    email_recipients = models.ManyToManyField(
        get_user_model(),
        blank=True,
        limit_choices_to={'is_staff': True},
        help_text='Contact form messages will be sent to these users, using their current email address.'
    )

    class Meta:
        verbose_name_plural = 'contact preferences'

    @property
    def emails_from_raw(self):
        if self.raw_emails:
            return [e.strip() for e in self.raw_emails.split('\n')]
        return []

    @property
    def emails(self):
        user_emails = list(self.email_recipients.values_list('email', flat=True))
        return user_emails + self.emails_from_raw


class StudentRegistrationPreferences(Preferences):
    __module__ = 'preferences.models'
    registration_form = models.ForeignKey(
        Form,
        null=True,
        blank=True,
        help_text="Students will use this form to register for a course."
    )
    registration_status = models.CharField(
        max_length=8,
        default='closed',
        choices=(
            ('open', 'Open'),
            ('closed', 'Closed')
        )
    )

    class Meta:
        verbose_name_plural = 'student registration preferences'


def set_form_status(sender, **kwargs):
    '''
    Publish/retract registration form based on the
    current registration status. The form url should
    return 404 if registrations are closed.
    '''
    try:
        if sender is StudentRegistrationPreferences:
            reg_prefs = kwargs['instance']
            form = reg_prefs.registration_form
        else:
            reg_prefs = preferences.StudentRegistrationPreferences
            form = kwargs['instance']
            if reg_prefs.registration_form_id != form.id:
                return

        if form.status == STATUS_DRAFT and \
                reg_prefs.registration_status == 'open':
            form.status = STATUS_PUBLISHED
            form.save(update_fields=['status'])
        elif form.status == STATUS_PUBLISHED and \
                reg_prefs.registration_status == 'closed':
            form.status = STATUS_DRAFT
            form.save(update_fields=['status'])
        
    except StudentRegistrationPreferences.DoesNotExist:
        pass


post_save.connect(set_form_status, sender=StudentRegistrationPreferences)
post_save.connect(set_form_status, sender=Form)
