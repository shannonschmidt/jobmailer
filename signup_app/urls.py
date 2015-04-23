from django.conf.urls import patterns, url
from signup_app import views
urlpatterns = patterns('',
                    url(r'^$',views.index,name='index'),


#Every view needs to be registered by a
    #url(pattern,view-identifier,view-name
)
