from django.views.generic import TemplateView
from django.views.generic.dates import ArchiveIndexView

from website.apps.posts.models import Post


class GenericContentView(TemplateView):
    template_name = 'core/generic_content.html'
    title = ''
    content = ''

    def get_context_data(self, **kwargs):
        context = super(GenericContentView, self).get_context_data(**kwargs)
        context['title'] = self.title
        context['content'] = self.content
        return context


class HomeView(ArchiveIndexView):
    template_name = 'core/home.html'
    context_object_name = 'posts'
    date_field = 'published_on'
    paginate_by = 2
    queryset = Post.objects.filter(published=True)


home = HomeView.as_view()
