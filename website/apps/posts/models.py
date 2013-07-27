from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from ckeditor.fields import RichTextField

from website.apps.posts.managers import PostManager


class Post(models.Model):

    objects = PostManager()

    title = models.CharField(max_length=128)
    description = models.CharField(max_length=128, null=True, blank=True)
    content = RichTextField()
    creator = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True)
    published = models.BooleanField(editable=False)
    published_on = models.DateTimeField(null=True, blank=True, editable=False)

    class Meta:
        ordering = ('-published_on', )

    def publish(self):
        if not self.published:
            self.published = True
            self.published_on = timezone.now()
            self.save()

    def unpublish(self):
        if self.published:
            self.published = False
            self.save()
