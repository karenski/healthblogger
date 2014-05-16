from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'blog.views.index', name='home'),
	url(r'^articles/$', 'blog.views.index', name='articles'),
	url(r'^tags/([\w-]+)/$', 'blog.views.tag'),
	url(r'^add_article/$', 'blog.views.add_article', name='add_article'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
