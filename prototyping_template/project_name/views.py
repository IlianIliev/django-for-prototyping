from django.views.generic import TemplateView


class StaticPageView(TemplateView):
    """ Static Page Template View """
    def get(self, request, slug=None): 
        if slug:
            self.template_name = '{{ project_name }}/%s.html' % slug
        return super(StaticPageView, self).get(request, slug)