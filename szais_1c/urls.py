"""szais_1c URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from main.views import *
from django.contrib.auth.views import login


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', index, name='index'),
    # url(r'^index/', index),
    # """Определяет схемы URL для пользователей"""
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^answer_inn/$',answer_inn, name='answer_inn'),
    url(r'^answer_sogl/$',answer_sogl, name='answer_sogl'),
    url(r'^search/$',search, name='search'),
    url(r'^info/$', info, name='info'),
    url(r'^affiliation/$', affiliation, name='affiliation'),
    # Страница выхода
    url(r'^logout/$', logout_view, name='logout'),
]