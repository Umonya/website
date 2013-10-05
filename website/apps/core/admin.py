from django.contrib import admin

from preferences.admin import PreferencesAdmin

from website.apps.core.models import ContactPreferences


admin.site.register(ContactPreferences, PreferencesAdmin)
