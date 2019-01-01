   # -*- coding: utf-8 -*-

from django.utils import translation
from django.conf import settings
#from django.core.cache import cache
#from people.helpers import get_current_language, get_or_create_person
#from license.models import SiteLicense
#from django.contrib.sites.shortcuts import get_current_site

from languages.models import Person

class LanguageMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        '''
        set_cookie = False
        if request.COOKIES.has_key(settings.LANGUAGE_COOKIE_NAME):
            language = request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME)
        elif hasattr(request, 'user'):
            if request.user.is_authenticated():
                current_language = get_current_language(request)
                if current_language:
                    set_cookie = True
        else:
            language = translation.get_language()
            # set_cookie = True
        '''

        #language = translation.get_language()
        qs = Person.objects.get(name='calves')
        
        
        language = qs.language

        print('language from Middleware: ' + language)

        translation.activate(language)
        request.LANGUAGE_CODE = translation.get_language()
        response = self.get_response(request)
        #print("response :" + str(response))

        '''
        if set_cookie:
            response.set_cookie(
                settings.LANGUAGE_COOKIE_NAME,
                language,
                max_age=2*365 * 24 * 60 * 60,
                domain=settings.SESSION_COOKIE_DOMAIN,
                secure=settings.SESSION_COOKIE_SECURE or None
            )
		'''

        # Code to be executed for each request/response after
        # the view is called.

        translation.deactivate()  # Deactivates our langauge after we've processed the request.
        return response

