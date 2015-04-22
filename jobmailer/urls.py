from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^signup_app/',include('signup_app.urls',namespace='signup_app')),
    url(r'^admin/', include(admin.site.urls)),
)