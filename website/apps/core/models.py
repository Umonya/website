from django.db import models
from django.contrib.auth import get_user_model

from preferences.models import Preferences


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
