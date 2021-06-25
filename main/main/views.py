from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.detail import DetailView

class HomePage(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context={'name':'hamza','study':'bsse','age':15,'pk':'pk'}
        print(kwargs)
        return context

class AboutPage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(kwargs)
        return context

