from django.shortcuts import render_to_response
from django.template import RequestContext

from website.apps.posts.models import Post


def home(request):
    return render_to_response('core/home.html',
                              {'posts': Post.objects.all()},
                              RequestContext(request))
