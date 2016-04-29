from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class IndexView(TemplateView):
    """Index view to home page"""

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context
