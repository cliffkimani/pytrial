from django.conf.urls import patterns, include, url


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    #===================== basic urls ============================#
    
    url(r'^$', 'writing.views.home', name='home'),
    url(r'^index.html$', 'writing.views.home', name='home'),
    
    
    #===================== admin urls ============================#
    
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),



    #===================== authentication urls ============================#
    url(r'^accounts/login/$', 'writing.views.login'),
    url(r'^accounts/auth/$', 'writing.views.auth_view'),
    url(r'^accounts/loggedin/accounts/logout/$', 'writing.views.logout'),
    url(r'^accounts/loggedin/$', 'writing.views.loggedin'),
    url(r'^accounts/invalid/$', 'writing.views.invalid_login'),
    
    )
