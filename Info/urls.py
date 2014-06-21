from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^init_county/$', 'Info.views.init_county'),
)