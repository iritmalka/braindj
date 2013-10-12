from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from django.views.generic import TemplateView

from braindj.views import state, play, next, get_current_song, pause, set_state, current_likeness

urlpatterns = patterns('',

    (r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^current_likeness/?$', current_likeness),
	url(r'^state/?$', state),
	url(r'^set_state/?$', set_state),
	url(r'^play/?$', play),
	url(r'^next/?$', next),
	url(r'^pause/?$', pause),
	url(r'^get_current_song/?$', get_current_song),
    
    # Examples:
    # url(r'^$', 'braindj.views.home', name='home'),
    # url(r'^braindj/', include('braindj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
