from django.contrib import admin

from preferences.admin import PreferencesAdmin

from website.apps.core.models import (ContactPreferences,
                                      GeneralPreferences,
                                      StudentRegistrationPreferences)


admin.site.register(ContactPreferences, PreferencesAdmin)
admin.site.register(GeneralPreferences, PreferencesAdmin)
admin.site.register(StudentRegistrationPreferences, PreferencesAdmin)
