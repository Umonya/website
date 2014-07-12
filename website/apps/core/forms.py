from contact_form.forms import ContactForm as BaseContactForm
from preferences import preferences


class ContactForm(BaseContactForm):

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        # add html5 required attribute
        for field in self.fields.values():
            if field.required:
                field.widget.attrs['required'] = ''

    def save(self, fail_silently=False):
        """
        Override so that we can get recipients list from
        preferences in database rather than MANAGERS setting
        """
        self.recipient_list = preferences.ContactPreferences.emails
        super(ContactForm, self).save(fail_silently)
