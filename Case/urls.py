from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^list/$', 'Case.views.case_list_view'),
    url(r'^json_list/$', 'Case.views.json_case_list'),
    url(r'^add/$', 'Case.views.add_case_view'),
    url(r'^accept/$', 'Case.views.accept_case')
)