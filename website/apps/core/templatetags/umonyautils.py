from django import template
from django.core.urlresolvers import reverse, NoReverseMatch


register = template.Library()


@register.tag
def active_path_class(parser, token):
    try:
        tag_name, view_name = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires exactly one argument"
                                           % token.contents.split()[0])
    return ActiveViewNode(view_name)


class ActiveViewNode(template.Node):

    def __init__(self, view_name):
        self.view_name = template.Variable(view_name)

    def render(self, context):
        view_name = self.view_name.resolve(context)
        try:
            url = reverse(view_name)
            if url == context['request'].path_info:
                return 'active'
        except NoReverseMatch:
            pass
        return ''
