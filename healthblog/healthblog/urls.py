from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'blog.views.index', name='home'),
	url(r'^articles/$', 'blog.views.index', name='articles'),
	url(r'^tags/([\w-]+)/$', 'blog.views.tag'),
	url(r'^add_article/$', 'blog.views.add_article', name='add_article'),
	url(r'^login/$', 'django.contrib.auth.views.login'),
	url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': "/"}),
	url(r'^register/$', 'blog.views.register', name='register'),
	url(r'^goto/$', 'blog.views.track_url', name='track_url'),
	url(r'^about/$', 'blog.views.about', name='about'),

    url(r'^admin/', include(admin.site.urls)),
)
