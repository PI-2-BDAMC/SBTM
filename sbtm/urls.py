from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views

import sbtmApp.views
import accounts.views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^startEngine/', sbtmApp.views.startEngine, name="startEngine"),
    url(r'^$', sbtmApp.views.index, name='index'),
    url(r'^signup/$', accounts.views.signup, name='signup'),
    url(r'^signin/$', accounts.views.signin, name='signin'),
    url(r'^previousTests/', sbtmApp.views.previousTests, name="previousTests"),
    url(r'^graphs/', sbtmApp.views.graphs, name="graphs"),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
]
