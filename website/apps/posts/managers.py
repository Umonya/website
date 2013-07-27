from django.db import models


class PostManager(models.Manager):

    def get_queryset(self, include_all=False):
        if not include_all:
            return super(PostManager, self).get_queryset().filter(published=True)
        return super(PostManager, self).get_queryset()
