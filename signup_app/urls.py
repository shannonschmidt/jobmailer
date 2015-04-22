from django.conf.urls import patterns, url
from signup_app import views
urlpatterns = patterns('',
                    url(r'^$',views.index,name='index'),
                    url(r'^$',views.submit_form,name='submit_form'),


#Every view needs to be registered by a
    #url(pattern,view-identifier,view-name
)
