from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Auth.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #user auth URLS
    url(r'^accounts/login/$','Skygraph.views.login'),
    url(r'^accounts/auth/$','Skygraph.views.auth_view'),
    url(r'^accounts/logout/$','Skygraph.views.logout'),
    url(r'^accounts/loggedin/$','Skygraph.views.loggedin'),
    url(r'^accounts/invalid/$','Skygraph.views.invalid_login'),
    url(r'^accounts/register/$','Skygraph.views.register_user'),

    url(r'^accounts/register_success/$','Skygraph.views.register_success'),

    #url(r'^accounts/Weather/area/$','Skygraph.views.test'),

    url(r'^Weather/', include('Skygraph.urls')),
    url(r'^list/', 'Skygraph.views.list'),
    url(r'^compare/', 'Skygraph.views.compare'),
    url(r'^export/', 'Skygraph.views.export')
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
