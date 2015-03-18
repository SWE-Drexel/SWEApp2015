from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('sweshare.views',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^home/', 'home', name='home'),
	url(r'^register/', 'register', name='register'),
	url(r'^loginpage/', 'loginpage', name='loginpage'),
	url(r'^goalpage/', 'goalpage', name='goalpage'),

)
