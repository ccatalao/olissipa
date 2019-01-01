from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
#from django.contrib.auth.views import LoginView, LogoutView

#from profiles.views import RegisterView, activate_user_view

from . import views

app_name = 'languages'

urlpatterns = [

    path('set_language_pt/',views.set_language_pt, name='set_language_pt'),
    path('set_language_en/',views.set_language_en, name='set_language_en'),
    url(r'^i18n/', include('django.conf.urls.i18n')),

    #url(r'^login/$', LoginView.as_view(), name='login'),
    #url(r'^logout/$', LogoutView.as_view(), name='logout'),
    #url(r'^register/$', RegisterView.as_view(), name='register'),
    #url(r'^activate/(?P<code>[a-z0-9].*)/$', activate_user_view, name='activate'),
    #path('', include('project.urls')),
]