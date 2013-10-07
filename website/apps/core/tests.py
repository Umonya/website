from django.contrib.sites.models import Site
from django.test import TestCase

from forms_builder.forms.models import Form, STATUS_PUBLISHED, STATUS_DRAFT

from website.apps.core.models import StudentRegistrationPreferences


class RegistrationTestCase(TestCase):

    def create_preferences(self, **fields):
        # can only have 1 instance per site
        StudentRegistrationPreferences.objects.all().delete()
        preferences = StudentRegistrationPreferences.objects.create(**fields)
        preferences.sites.add(Site.objects.get_current())
        return preferences

    def create_form(self, **fields):
        form = Form.objects.create(**fields)
        form.sites.add(Site.objects.get_current())
        return form

    def test_open_registration(self):
        form = self.create_form(title='Foo')
        preferences = self.create_preferences(registration_form=form)
        # check that form is not published
        self.assertFalse(Form.objects.published().filter(id=form.id).count())
        # open registrations
        preferences.registration_status = 'open'
        preferences.save()
        # check that form is now published
        self.assertEqual(Form.objects.published().filter(id=form.id).count(), 1)
        # try to unpublish form and make sure it fails
        form.status = STATUS_DRAFT
        form.save()
        self.assertEqual(Form.objects.get(id=form.id).status, STATUS_PUBLISHED)

    def test_close_registration(self):
        form = self.create_form(title='Foo', status=STATUS_PUBLISHED)
        preferences = self.create_preferences()
        # check that form is published
        self.assertEqual(Form.objects.published().filter(id=form.id).count(), 1)
        # assign form to closed registrations
        preferences.registration_form = form
        preferences.save()
        # check that form is no longer published
        self.assertFalse(Form.objects.published().filter(id=form.id).count())
        # try to publish form and make sure it fails
        form.status = STATUS_PUBLISHED
        form.save()
        self.assertEqual(Form.objects.get(id=form.id).status, STATUS_DRAFT)
