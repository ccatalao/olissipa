from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
# The django internationalization lib
from django.utils.translation import ugettext_lazy as _
#from django.utils.translation import ugettext as _, ugettext
from django.utils.translation import LANGUAGE_SESSION_KEY

from django.utils import translation

from .models import Person


def set_language_en(request):
    
    user_language = 'en-us' 

    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    request.session['django_language'] = user_language          
    
    try:
    	qs = Person.objects.get(name='calves')
    except:
    	pass

    if qs:
    	qs.language='en-us'
    	qs.save()

    
    return render(request, 'index.html', {})



def set_language_pt(request):

    user_language = 'pt-pt' 

    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    request.session['django_language'] = user_language      

    try:
    	qs = Person.objects.get(name='calves')
    except:
    	pass

    if qs:
    	qs.language='pt-pt'
    	qs.save()

    
    return render(request, 'index.html', {})

    