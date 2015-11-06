"""login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import login, logout
#from article import settings
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', 'article.views.hello'),
    #url(r'^home/$', 'article.views.auth_view'),
    #url(r'^$', 'article.views.auth_view'),
    url(r'^language/$', 'article.views.language'),
    url(r'^article/$', 'article.views.articles'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'main.html'}),
    url(r'^home/$', 'django.contrib.auth.views.login', {'template_name': 'main.html'}),
    url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'main.html'}),
    #url(r'^login/$', 'article.views.auth_view'),
    #url(r'^auth/$', 'article.views.auth_view'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}),
    #url(r'^logout/$', 'article.views.logout'),
    url(r'^welcome/$', 'article.views.welcome'),
    url(r'^invalid/$', 'article.views.invalid_login'),
    #url(r'^accounts/login/$', 'article.views.home'),
]
urlpatterns += staticfiles_urlpatterns()
