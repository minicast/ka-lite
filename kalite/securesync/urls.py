from django.http import HttpResponse, HttpResponseRedirect
from django.conf.urls.defaults import patterns, include, url
import views

urlpatterns = patterns('securesync.api_views',
    url(r'^api/register$', 'register_device', {}, 'register_device'),
    url(r'^api/test$', 'test_connection', {}, 'test_connection'),
    url(r'^api/session/create$', 'create_session', {}, 'create_session'),
    url(r'^api/session/destroy$', 'destroy_session', {}, 'destroy_session'),
    url(r'^api/device/counters$', 'device_counters', {}, 'device_counters'),
    url(r'^api/device/download$', 'device_download', {}, 'device_download'),
    url(r'^api/models/download$', 'download_models', {}, 'download_models'),
    url(r'^api/models/upload$', 'upload_models', {}, 'upload_models'),
    url(r'^api/status$', 'status', {}, 'status'),
)

urlpatterns += patterns('securesync.views',
    url(r'^register/$', 'register_public_key', {}, 'register_public_key'),
    url(r'^addteacher/$', 'add_facility_teacher', {}, 'add_facility_teacher'),
    url(r'^addstudent/$', 'add_facility_student', {}, 'add_facility_student'),
    url(r'^facility/new/$', 'add_facility', {}, 'add_facility'),
    url(r'^facilityselection/$', 'facility_selection', {}, 'facility_selection'),
    url(r'^facilityadmin/$', 'facility_admin', {}, 'facility_admin'),
    url(r'^addgroup/$', 'add_group', {}, 'add_group'),
    url(r'^login/$', 'login', {}, 'login'),
    url(r'^logout/$', 'logout', {}, 'logout'),
)
