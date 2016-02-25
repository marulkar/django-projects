"""myprojects URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^projects/', include('projects.urls')),
    url(r'^accounts/login/$',  'myprojects.views.login'),
    url(r'^accounts/auth/$',  'myprojects.views.auth_view'),    
    url(r'^accounts/logout/$', 'myprojects.views.logout'),
    url(r'^accounts/loggedin/$', 'myprojects.views.loggedin'),
    url(r'^accounts/invalid/$', 'myprojects.views.invalid_login'), 
    url(r'^accounts/register/$', 'myprojects.views.register_user'),
    url(r'^accounts/register_success/$', 'myprojects.views.register_success'),
]
