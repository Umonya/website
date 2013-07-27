from django.contrib import admin
from django.utils import timezone
from django.template.defaultfilters import truncatechars

from website.apps.posts import models


class PostAdmin(admin.ModelAdmin):
    actions = ('publish', 'unpublish')
    list_display = ('title', 'truncated_description', 'creator',
                    'published', 'published_on', 'modified', 'created')

    def get_form(self, request, obj=None, **kwargs):
        form = super(PostAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['creator'].initial = request.user
        return form

    def publish(self, request, queryset):
        queryset.filter(published=False).update(published=True,
                                                published_on=timezone.now())

    def unpublish(self, request, queryset):
        queryset.filter(published=True).update(published=False)

    def truncated_description(self, instance):
        return truncatechars(instance.description, 64)
    truncated_description.short_description = 'description'


admin.site.register(models.Post, PostAdmin)
