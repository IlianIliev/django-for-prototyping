from django.conf import settings
from django.http import Http404
from django.template import TemplateDoesNotExist
from django.views.generic import TemplateView


class StaticPageView(TemplateView):
    """ Static Page Template View """
    def get(self, request, slug=None): 
        if slug:
            self.template_name = '{{ project_name }}/%s.html' % slug
            request.page = slug
        else:
            request.page = 'home'
        result = super(StaticPageView, self).get(request, slug)
        if not settings.DEBUG:
            try:
                result.resolve_template(self.template_name)
            except TemplateDoesNotExist, e:
                raise Http404
        return result
