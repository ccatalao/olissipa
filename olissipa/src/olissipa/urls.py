from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin

from django.conf.urls.i18n import i18n_patterns

from olissipa import views

from .views import (
    IndexView,
    AboutView,
)

urlpatterns = [
	path('admin/', admin.site.urls),
    path('',IndexView.as_view(), name='index'),
    path('pt-pt/about/',AboutView.as_view(),name='about'),
    path('en-us/about/',AboutView.as_view(),name='about'),
    path('languages/',include('languages.urls'), name='languages'),
    path('accounts/', include('allauth.urls')),

]

urlpatterns += i18n_patterns(
    path('about/', AboutView.as_view(), name='about'),
)