from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings

from django.utils.translation import ugettext_lazy as _

class IndexView(TemplateView):
    template_name = 'index.html'


    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs) 

        return context


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
 
        return context
